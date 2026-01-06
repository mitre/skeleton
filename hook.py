from app.utility.base_world import BaseWorld
from plugins.menupass_port.app.menupass_port_gui import Menupass_portGUI
from plugins.menupass_port.app.menupass_port_api import Menupass_portAPI

name = 'Menupass_port'
description = 'Porting menuPass from CTID AEL into caldera'
address = '/plugin/menupass_port/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    menupass_port_gui = Menupass_portGUI(services, name=name, description=description)
    app.router.add_static('/menupass_port', 'plugins/menupass_port/static/', append_version=True)
    app.router.add_route('GET', '/plugin/menupass_port/gui', menupass_port_gui.splash)

    menupass_port_api = Menupass_portAPI(services)
    # Add API routes here
    app.router.add_route('POST', '/plugin/menupass_port/mirror', menupass_port_api.mirror)

