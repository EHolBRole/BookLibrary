import Infrastructure.handlers as h
import Exceptions.exceptions as e


class InfrastructureAPI:
    def __init__(self, handler: h.Handler):
        self.handler = handler
        pass

    def push_data(self, data):
        self.handler.push_data(data)

    def get_data(self):
        return self.handler.get_data()
    pass


def get_api(handler_type):  # NOTE: Think about Abstract Fabric pattern
    handlers = {h.JsonHandler('JSON/library.json')}

    for handler in handlers:
        if handler_type == handler.h_type:
            return InfrastructureAPI(handler)
    else:
        raise e.HandlerException('Invalid handler type.')
    pass


