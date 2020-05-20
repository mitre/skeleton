from app.utility.base_world import BaseWorld
from plugins.skeleton.app.skeleton_gui import SkeletonGui

name = 'Skeleton'
description = 'some good bones'
address = '/plugin/skeleton/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    skeleton_gui = SkeletonGui(services)
    app.router.add_static('/skeleton', 'plugins/skeleton/static/', append_version=True)
    app.router.add_route('GET', '/plugin/skeleton/gui', skeleton_gui.splash)
    app.router.add_route('*', '/plugin/skeleton/api', skeleton_gui.skeleton_core)
    app.router.add_route('POST', '/plugin/skeleton/upload', skeleton_gui.store_file)

