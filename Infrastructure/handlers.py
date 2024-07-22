import json
import Domain.entities as e
import Infrastructure.handler_enum as he

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, h_type):
        self.h_type = h_type
        pass

    @abstractmethod
    def push_data(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass

    pass


class JsonHandler(Handler):
    def __init__(self):
        super().__init__(he.Handlers.JSON)
        self.address = 'JSON/library.json'

    def get_data(self):
        with open(self.address, 'r+') as f:
            data = json.load(f)
        return data

    def push_data(self, data):
        if isinstance(data, e.Book):
            try:
                with open(self.address, 'r+') as f:
                    library_data = json.load(f)
                    if len(list(library_data)) != 0:
                        nk = 1 + int(list(library_data)[-1])
                    else:
                        nk = 1 + 0
                    library_data[nk] = data.__dict__
                    with open(self.address, 'w') as fi:
                        json.dump(library_data, fi)
                pass
            except json.decoder.JSONDecodeError:
                with open(self.address, 'w+') as f:
                    json.dump({1: data.__dict__}, f)
                pass
        else:
            with open(self.address, 'w+') as f:
                json.dump(data, f)

    pass
