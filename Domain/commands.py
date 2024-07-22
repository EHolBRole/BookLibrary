import Exceptions.exceptions as ex
import Infrastructure.infrastructure_api as i_api
import Application.application_dto as a_dto

from Domain.entities import Book
from abc import ABC, abstractmethod
from api_library import LibraryAPI as l_api


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


class ExitAppCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        if len(args) != 0:
            return False
        return True

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            raise ex.FinishInterpretationException('Exit exception!')
        else:
            raise ex.ExitCommandException('Invalid input!')

    def __init__(self):
        super().__init__('exit')


class AddBookCommand(Command):
    def __init__(self):
        super().__init__('add')
        self.lib_address = None

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            book = Book(args[0], args[1], args[2])
            l_api.infrastructure_api.push_data(book)
            return True
        else:
            raise ex.AddCommandException('Invalid input!')
        pass

    def is_user_input_valid(self, args: list[str]):
        if len(args) != 3:
            return False
        return True
    pass


class RemoveBookCommand(Command):

    def __init__(self):
        super().__init__('rm')
        self.lib_address = None

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            library_data.pop(args[0])
            l_api.infrastructure_api.push_data(library_data)
            return True
        else:
            raise ex.RemoveCommandException("Invalid input!")
        pass

    def is_user_input_valid(self, args: list[str]):
        if not args[0].isdigit():
            return False
        if len(args) > 1:
            return False
        return True


class FindBookCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        if len(args) != 1:
            return False
        return True
        pass

    def __init__(self):
        super().__init__('find')
        self.lib_address = None

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            response_data = list()
            for book in library_data:
                if library_data[book]['title'] == args[0]:
                    response_data.append(library_data[book])
                elif library_data[book]['author'] == args[0]:
                    response_data.append(library_data[book])
                elif library_data[book]['year'] == args[0]:
                    response_data.append(library_data[book])
            return a_dto.ApplicationDTOResponse(response_data)
        else:
            raise ex.FindCommandException("Invalid input!")
        pass


class ShowBooksCommand(Command):
    def is_user_input_valid(self, args: list[str]):
        return True

    def __init__(self):
        super().__init__('ls')
        self.lib_address = None

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            response_data = list()
            for book in library_data:
                response_data.append(library_data[book])
            return a_dto.ApplicationDTOResponse(response_data)
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

    def __init__(self):
        super().__init__('schange')
        self.lib_address = None

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            library_data[args[0]]['status'] = args[1]
            l_api.infrastructure_api.push_data(library_data)
            return True
        else:
            raise ex.ChangeCommandException("Invalid input!")
        pass
