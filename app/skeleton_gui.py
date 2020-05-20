import json
import logging
from aiohttp import web
from aiohttp_jinja2 import template

from app.service.auth_svc import check_authorization
from app.utility.base_world import BaseWorld
from plugins.skeleton.app.skeleton_svc import SkeletonService


class SkeletonGui(BaseWorld):

    def __init__(self, services):
        self.services = services
        self.skeleton_svc = SkeletonService(services)
        self.auth_svc = services.get('auth_svc')
        self.file_svc = services.get('file_svc')
        self.log = logging.getLogger('skeleton_gui')

    @check_authorization
    @template('skeleton.html')
    async def splash(self, request):
        return dict(initial_data=['option 1', 'option 2', 'option 3'])

    @check_authorization
    async def skeleton_core(self, request):
        try:
            data = dict(await request.json())
            index = data.pop('index')
            options = dict(
                DELETE=dict(),
                PUT=dict(),
                POST=dict(
                    do_something=lambda d: self.something(),
                    process_file=lambda d: self.process_file(d)  # d is the data dict with index popped off
                )
            )
            if index not in options[request.method]:
                return web.HTTPBadRequest(text='index: %s is not a valid index for the skeleton plugin' % index)
            return web.json_response(await options[request.method][index](data))
        except Exception as e:
            self.log.error(repr(e), exc_info=True)

    async def something(self):
        response = await self.skeleton_svc.something()
        return dict(output=response)

    async def process_file(self, data):
        await self.skeleton_svc.do_file_thing(data['filename'], data['option'])
        return dict(output='%s: successfully did something with %s' % (data['option'], data['filename']))

    @check_authorization
    async def store_file(self, request):
        return await self.file_svc.save_multipart_file_upload(request, 'plugins/skeleton/data/uploads/')
