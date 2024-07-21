import handlers


class InfrastructureAPI:
    def __init__(self, handler: handlers.Handler):
        self.handler = handler
        pass

    def push_data(self, data):
        self.handler.push_data(data)

    def get_data(self, data):
        return self.handler.get_data(data)
    pass
