from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self, args: list[str]):
        pass

    pass


class AddBookCommand(Command):
    def __init__(self):
        super().__init__("add")

    def execute(self, args: list[str]):
        pass

    pass


class RemoveBookCommand(Command):
    def __init__(self):
        super().__init__("rm")

    def execute(self, args: list[str]):
        pass

    pass


class FindBookCommand(Command):
    def __init__(self):
        super().__init__("find")

    def execute(self, args: list[str]):
        pass

    pass


class ShowBooksCommand(Command):
    def __init__(self):
        super().__init__("ls")

    def execute(self, args: list[str]):
        pass

    pass


class ChangeBookStatusCommand(Command):
    def __init__(self):
        super().__init__("schange")

    def execute(self, args: list[str]):
        pass

    pass
