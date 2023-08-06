"""
Provides the @route decorator and its implementation.

The decorator creates a DynamicRoute object, defined here, and stores it in the global
list of routes (`_routes`).  There is also a lookup function to find the
appropriate route for a URL.
"""

# REVIEW: We could implement static files as middleware, but I don't
# want to pay the performance penalty.  A single page app is rarely
# going to load a static file.  Also, if it is a big app it might be
# using a CDN or proxy and never load a static file

import re, inspect
from urllib.parse import urlparse
from asyncio import coroutine
from .middleware import middleware

_routes = []
# The global list of registered routes as DynamicRoute objects.


def register_route(r):
    for m in middleware:
        m.register_route(r)
    _routes.append(r)


def route(pattern, *, method=None, **kwargs):
    """
    The @route decorator used to register URL handlers.  The first parameter of
    the decorated function should be named "ctx".

    pattern
      The pattern for the URL the decorated function will handle.

      Wrap a component of the path in braces to mark it as a variable
      ("/file/{filename}").  The decorated function must take a parameter with
      this name.

    logger
      Optional Python logging.Logger instance.  If provided, the route
      parameters will be logged to it using logger.debug.
    """
    s = inspect.stack()
    logger = s[2].frame.f_globals.get('logger')

    assert method, 'Forgot to set "method" keyword in @route for %r.  You probably want to use @get or @post.' % pattern
    assert method in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'), 'invalid method: %r' % method

    def wrapper(func):
        # TODO: Convert to "==".
        assert not _find(pattern), 'URL "{}" registered twice: first={} second={}'.format(pattern, _find(pattern).funcname, func.__name__)

        r = DynamicRoute(pattern, func, kwargs, method=method, logger=logger)
        for m in middleware:
            m.register_route(r)

        _routes.append(r)
    return wrapper


def get(pattern, **kwargs):
    # You use "method" to set the method, but the point of having a function named "get" is to
    # set the method to "GET".  If you need another method, use @route instead.
    assert 'method' not in kwargs, 'Do not use "method" with get.  Use @route if you need another method.'
    kwargs['method'] = 'GET'
    return route(pattern, **kwargs)

def post(pattern, **kwargs):
    assert 'method' not in kwargs, 'Do not use "method" with post.  Use @route if you need another method.'
    kwargs['method'] = 'POST'
    return route(pattern, **kwargs)

def put(pattern, **kwargs):
    assert 'method' not in kwargs, 'Do not use "method" with put.  Use @route if you need another method.'
    kwargs['method'] = 'PUT'
    return route(pattern, **kwargs)

def delete(pattern, **kwargs):
    assert 'method' not in kwargs, 'Do not use "method" with delete.  Use @route if you need another method.'
    kwargs['method'] = 'DELETE'
    return route(pattern, **kwargs)


def _find(pattern):
    for r in _routes:
        if getattr(r, 'pattern', None) == pattern:
            return r
    return None

def find(method, url):
    """
    Given a URL, find the Route that handles it.

    If found, a tuple containing the Route object and the regular expression match used to
    match the pattern is returned.  If there are variables in the URL, the match will have a
    group for each in the order they are found in the URL.

    If not found, (None, None) is returned.
    """
    assert method in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'), 'Invalid method %r' % method

    url = urlparse(url)

    for r in _routes:
        if r.method != method:
            continue

        match = r.regexp.match(url.path)
        if match:
            return (r, match)

    return (None, None)


class Route:
    """
    The base class for routes.
    """
    def __init__(self, route_keywords=None, *, method, logger=None):
        self.route_keywords = route_keywords or {}
        self.method = method
        self.logger = logger


class DynamicRoute(Route):
    """
    A route that calls a user-defined function.  Instances of this are
    registered by the @route decorator.

    Variables can be created in the URL pattern by wrapping components
    in braces, such as "/static/js/{filename}".

    This object is callable like a function and will pick the arguments to the
    URL handler from the request (GET variables, JSON variables, etc.)
    """
    def __init__(self, pattern, func, route_keywords, *, method, logger=None):
        """
        pattern
          The URL regexp.

        func
          The URL handler callback.

        route_keywords
          A dictionary of keyword arguments passed to the @route decorator.
        """
        Route.__init__(self, route_keywords=route_keywords, logger=logger, method=method)

        self.pattern = pattern
        self._func = func
        self.func = coroutine(func)

        self.regexp = None

        self.urlvars = []
        # The names of variables to be parsed from the URL, in the order they
        # appear in the pattern.  There is a group for each in `self.regexp` so
        # all we have to do is get all of the groups.

        self.formvars = []
        # The names of variables we expect to find in vars variables or a JSON
        # object (depending on the content-type).  These are the URL handler
        # parameters that are not variables in the URL pattern.

        self.annotations = {}
        # The optional annotations describing the argument types for the URL handler function.
        #
        # This is the annotations from `inspect.getfullargspect`.  It is a mapping from
        # argument name to its type.  Only arguments that have an annotation are present.
        #
        # This is available to the functions reading URL and form variables to provide for
        # custom conversions, such as from an encoded Javascript date to a Python date,
        # datetime, or time.  (Javascript's Date always has date and time components, so by
        # annotating the server component, the system can remove the date or time as necessary
        # to get exactly the data type.)

        self.analyze_pattern()
        self.analyze_params()

    def analyze_params(self):
        """
        Analyzes the URL handlers parameters to determine which should come from URL
        variables and which are expected to be in the body.
        """
        spec = inspect.getfullargspec(self._func)

        if spec.annotations:
            self.annotations = spec.annotations

        assert spec.args and spec.args[0] == 'ctx', 'The first parameter is not `ctx`.  pattern={} callback={}'.format(self.pattern, self._func)

        args = set(spec.args[1:])
        self.formvars = args - set(self.urlvars)

    def analyze_pattern(self):
        """
        Creates a regular expression from the pattern for matching URLs.
        """
        # Split the URL by slashes and examine each part.  Each could be either
        # plan text (e.g. "static") or a variables (e.g. "{filename}").

        if self.pattern in ('/*', '*'):
            # handle catch all route
            self.regexp = re.compile('^/.*')
            self.urlvars = []
        else:
            assert self.pattern.startswith('/'), 'DynamicRoute patterns must start with "/": {!r}'.format(self.pattern)

            regexps  = []
            varnames = []

            for part in self.pattern.rstrip('/').split('/'):
                if part.startswith('{') and part.endswith('}'):
                    # variable
                    varnames.append(part[1:-1])
                    regexps.append('([^/]+)')
                else:
                    # plain text
                    regexps.append(re.escape(part))

            regexp = '^' + '/'.join(regexps) + '/?$'

            self.regexp = re.compile(regexp)
            self.urlvars = varnames


    @coroutine
    def __call__(self, match, ctx):
        """
        Calls the URL handler, passing any defined parameters.
        """
        args = {
            'ctx': ctx
        }

        if self.urlvars:
            args.update(zip(self.urlvars, match.groups()))

        if self.formvars and ctx.request.form:
            args.update({ name: ctx.request.form.get(name, None) for name in self.formvars })

        if self.logger:
            self.logger.debug('start: %s params=%r', self.pattern, args)

        result = yield from self.func(**args)

        if self.logger:
            self.logger.debug('complete: %s result=%r', self.pattern, result)

        return result

    def __repr__(self):
        return 'DynamicRoute<{} {}>'.format(self.pattern, self._func)

    @property
    def funcname(self):
        return self._func.__name__
