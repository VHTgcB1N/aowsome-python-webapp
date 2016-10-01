# coding = utf-8
import asyncio
import os
import inspect
import logging
import functools

from urllib import parse

from aiohttp import web

from apis import APIError


def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator


def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (
        method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))


class RequestHandler(object):
    """docstring for RequestHandler"""

    def __init__(self, app, fn):
        super(RequestHandler, self).__init__()
        self._app = app
        self._fn = fn

    async def __call__(self, request):
        kw = ...
        r = await self._func(**kw)
        return r
