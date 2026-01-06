import logging
from aiohttp_jinja2 import template

from app.service.auth_svc import for_all_public_methods, check_authorization
from app.utility.base_world import BaseWorld
from plugins.menupass_port.app.menupass_port_svc import Menupass_portService


@for_all_public_methods(check_authorization)
class Menupass_portGUI(BaseWorld):

    def __init__(self, services, name, description):
        self.name = name
        self.description = description
        self.services = services
        self.menupass_port_svc = Menupass_portService(services)

        self.auth_svc = services.get('auth_svc')
        self.log = logging.getLogger('menupass_port_gui')

    @template('menupass_port.html')
    async def splash(self, request):
        return dict(name=self.name, description=self.description)

    # Add functions here that the front-end will use

