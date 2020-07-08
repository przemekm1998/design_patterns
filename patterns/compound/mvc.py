from typing import Dict, KeysView


class Model:
    services: Dict[str, Dict[str, int]] = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10}
    }


class View:
    def list_services(self, services: KeysView[str]):
        for svc in services:
            print(svc, '')

    def list_pricing(self, services: KeysView[str]):
        for svc in services:
            print(f"For {Model.services[svc]['number']} you pay "
                  f"{Model.services[svc]['price']}")


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)


class Client:
    controller = Controller()
    print('Services provided', controller.get_services())
    
    print('prices', controller.get_pricing())