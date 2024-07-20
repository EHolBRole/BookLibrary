import json
import Exceptions.exceptions as ex

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
        else:
            raise ex.AddCommandException('Invalid input!')
        pass

    def is_user_input_valid(self, args: list[str]):
        if len(args) != 3:
            return False
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
        else:
            raise ex.RemoveCommandException("Invalid input!")
        pass

    def is_user_input_valid(self, args: list[str]):
        if not args[0].isdigit():
            return False
        if len(args) > 1:
            return False


class FindBookCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        if len(args) != 1:
            return False
        return True
        pass

    def __init__(self):
        super().__init__("find")

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            with open('../JSON/library.json', 'r+') as f:
                library_data = json.load(f)
                for book in library_data:
                    if library_data[book]['title'] == args[0]:
                        print(library_data[book])
                    elif library_data[book]['author'] == args[0]:
                        print(library_data[book])
                    elif library_data[book]['year'] == args[0]:
                        print(library_data[book])
        else:
            raise ex.FindCommandException("Invalid input!")
        pass


class ShowBooksCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        return True

    def __init__(self):
        super().__init__("ls")

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            with open('../JSON/library.json', 'r+') as f:
                library_data = json.load(f)
                for book in library_data:
                    print(library_data[book])
        else:
            raise ex.ShowCommandException("Invalid input!")
        pass


class ChangeBookStatusCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        if len(args) != 2:
            return False
        if args[1] == "stocked" or args[1] == "given":
            return True
        return False
        pass

    def __init__(self):
        super().__init__("schange")

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            with open('../JSON/library.json', 'r+') as f:
                library_data = json.load(f)
                library_data[args[0]]['status'] = args[1]
                with open('../JSON/library.json', 'w') as fi:
                    json.dump(library_data, fi)
        else:
            raise ex.ChangeCommandException("Invalid input!")
        pass
