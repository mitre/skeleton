from app.utility.base_world import BaseWorld
from plugins.skeleton.app.skeleton_gui import SkeletonGUI
from plugins.skeleton.app.skeleton_api import SkeletonAPI

name = 'Skeleton'
description = 'description'
address = '/plugin/skeleton/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    skeleton_gui = SkeletonGUI(services, name=name, description=description)
    app.router.add_static('/skeleton', 'plugins/skeleton/static/', append_version=True)
    app.router.add_route('GET', '/plugin/skeleton/gui', skeleton_gui.splash)

    skeleton_api = SkeletonAPI(services)
    # Add API routes here
    app.router.add_route('POST', '/plugin/skeleton/mirror', skeleton_api.mirror)

