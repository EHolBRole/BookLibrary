import unittest

import Exceptions.exceptions as ex
import Infrastructure.infrastructure_api as i_api
import Domain.domain_dto as d_dto

from Domain.entities import Book
from abc import ABC, abstractmethod
from api_library import LibraryRepository as l_api


class Command(ABC):  # Pattern Command used. This is abstract class for all commands.
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self, args: list[str]):
        pass

    @abstractmethod
    def is_user_input_valid(self, args: list[str]):
        pass

    pass


class ExitAppCommand(Command):  # Exit App Command realisation
    def __init__(self):
        super().__init__('exit')

    def is_user_input_valid(self, args: list[str]):
        if len(args) != 0:
            return False
        return True

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            raise ex.FinishInterpretationException('Exit exception!')
        else:
            raise ex.ExitCommandException('Invalid input!')


class AddBookCommand(Command):  # Add Book Command realisation
    def __init__(self):
        super().__init__('add')

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            book = Book(args[0], args[1], args[2])
            l_api.infrastructure_api.push_data(book)
            return d_dto.DomainDTOResponse([], True)
        else:
            raise ex.AddCommandException('Invalid input!')
        pass

    def is_user_input_valid(self, args: list[str]):
        if len(args) != 3:
            return False
        return True
    pass


class RemoveBookCommand(Command):  # Remove Book Command realisation

    def __init__(self):
        super().__init__('rm')

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            try:
                library_data.pop(args[0])
            except KeyError:
                raise ex.RemoveCommandException('Incorrect ID!')
            l_api.infrastructure_api.push_data(library_data)
            return d_dto.DomainDTOResponse([], True)
        else:
            raise ex.RemoveCommandException("Invalid input!")
        pass

    def is_user_input_valid(self, args: list[str]):
        if not args[0].isdigit():
            return False
        if len(args) > 1:
            return False
        return True


class FindBookCommand(Command):  # Find Book Command realisation
    def is_user_input_valid(self, args: list[str]):
        if len(args) != 1:
            return False
        return True
        pass

    def __init__(self):
        super().__init__('find')

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
            return d_dto.DomainDTOResponse(response_data, True)
        else:
            raise ex.FindCommandException("Invalid input!")
        pass


class ShowBooksCommand(Command):  # Show Book Command realisation
    def is_user_input_valid(self, args: list[str]):
        if len(args) > 0:
            return False
        return True

    def __init__(self):
        super().__init__('ls')

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            response_data = list()
            for book in library_data:
                response_data.append(library_data[book])
            return d_dto.DomainDTOResponse(response_data, True)
        else:
            raise ex.ShowCommandException("Invalid input!")
        pass


class ChangeBookStatusCommand(Command):  # Change Book Status Command realisation
    def is_user_input_valid(self, args: list[str]):
        if len(args) != 2:
            return False
        if args[1] == "stocked" or args[1] == "given":
            return True
        return False

    def __init__(self):
        super().__init__('schange')

    def execute(self, args: list[str]):
        if self.is_user_input_valid(args):
            library_data = l_api.infrastructure_api.get_data()
            library_data[args[0]]['status'] = args[1]
            l_api.infrastructure_api.push_data(library_data)
            return d_dto.DomainDTOResponse([], True)
        else:
            raise ex.ChangeStatusCommandException("Invalid input!")
        pass
