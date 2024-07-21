class AddCommandException(Exception):
    pass


class RemoveCommandException(Exception):
    pass


class FindCommandException(Exception):
    pass


class ShowCommandException(Exception):
    pass


class ChangeCommandException(Exception):
    pass


class IncorrectCommandException(Exception):
    pass


class ExitCommandException(Exception):
    pass


class FinishInterpretationException(Exception):
    pass
