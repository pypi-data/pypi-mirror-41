from asyncio import shield
from functools import update_wrapper
from typing import Type

from aiohttp import web
from buildpg.asyncpg import BuildPgConnection
from pydantic import BaseModel

from ..utils import json_response, parse_request_json


class View:
    __slots__ = 'request', 'app', 'conn', 'settings'

    def __init__(self, request):
        self.request: web.Request = request
        self.app: web.Application = request.app
        self.conn: BuildPgConnection = request.get('conn')
        self.settings = self.app['settings']

    @classmethod
    def view(cls):
        async def view(request):
            self: cls = cls(request)
            await self.check_permissions()
            return await self.call()

        view.view_class = cls

        # take name and docstring from class
        update_wrapper(view, cls, updated=())
        # and possible attributes set by decorators
        update_wrapper(view, cls.call, assigned=())
        return view

    async def check_permissions(self):
        pass

    async def call(self):
        raise NotImplementedError


class ExecView(View):
    Model: Type[BaseModel] = NotImplemented

    async def execute(self, m: Model):
        raise NotImplementedError

    async def call(self):
        m = await parse_request_json(self.request, self.Model)
        response_data = await shield(self.execute(m))
        response_data = response_data or {'status': 'ok'}
        return json_response(**response_data)
