import json
from Library.library_model import Book

from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self, args: list[str]):
        pass

    @abstractmethod
    def is_user_input_valid(self, args: list[str]):
        pass
    pass


class AddBookCommand(Command):
    def __init__(self):
        super().__init__("add")

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            book = Book(args[0], args[1], args[2])
            self.parse_book_to_json(book)
        pass

    def is_user_input_valid(self, args: list[str]):
        try:
            if len(args) != 3:
                raise Exception()
        except:  # TODO: Add unique exceptions
            return False
            pass
        return True

    def parse_book_to_json(self, book: Book):
        try:
            with open('../JSON/library.json', 'r+') as f:
                library_data = json.load(f)
                nk = 1 + int(list(library_data)[-1])
                library_data[nk] = book.__dict__
                with open('../JSON/library.json', 'w') as fi:
                    json.dump(library_data, fi)
            pass
        except json.decoder.JSONDecodeError:
            with open('../JSON/library.json', 'w+') as f:
                json.dump({1: book.__dict__}, f)
            pass
    pass


class RemoveBookCommand(Command):

    def __init__(self):
        super().__init__("rm")

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            with open('../JSON/library.json', 'r+') as f:
                library_data = json.load(f)
                library_data.pop(args[0])
                with open('../JSON/library.json', 'w') as fi:
                    json.dump(library_data, fi)
        pass

    def is_user_input_valid(self, args: list[str]):
        try:
            check = int(args[0])
            if len(args) > 1:
                return False
        except:
            return False
        return True


class FindBookCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        pass

    def __init__(self):
        super().__init__("find")

    def execute(self, args: list[str]):
        pass


class ShowBooksCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        pass

    def __init__(self):
        super().__init__("ls")

    def execute(self, args: list[str]):
        pass


class ChangeBookStatusCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        pass

    def __init__(self):
        super().__init__("schange")

    def execute(self, args: list[str]):
        pass
