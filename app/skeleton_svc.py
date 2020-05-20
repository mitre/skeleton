import logging


class SkeletonService:
    def __init__(self, services):
        self.services = services
        self.file_svc = services.get('file_svc')
        self.log = logging.getLogger('skeleton_svc')

    async def something(self):
        return 'I did something'

    async def do_file_thing(self, filename, option):
        _, contents = await self.file_svc.read_file(filename, location='uploads')
        self.log.debug(contents)
