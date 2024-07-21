from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def push_data(self, data):
        pass

    @abstractmethod
    def get_data(self, data):
        pass

    pass


class JsonHandler(Handler):
    def __init__(self, address):
        self.address = address
        pass

    def get_data(self, data):
        return data

    def push_data(self, data):
        pass

    pass
