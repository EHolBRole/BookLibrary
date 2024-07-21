import DDD.Infrastructure.handlers as h


class InfrastructureAPI:
    def __init__(self, handler: h.Handler):
        self.handler = handler
        pass

    def push_data(self, data):
        self.handler.push_data(data)

    def get_data(self):
        return self.handler.get_data()
    pass


infrastructure_api = InfrastructureAPI(h.JsonHandler('../../JSON/library.json'))
