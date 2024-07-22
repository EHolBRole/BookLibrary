class AddCommandException(Exception):  # Exception for Add command
    pass


class RemoveCommandException(Exception):  # Exception for Remove command
    pass


class FindCommandException(Exception):  # Exception for Find command
    pass


class ShowCommandException(Exception):  # Exception for Show command
    pass


class ChangeStatusCommandException(Exception):  # Exception for Change Status command
    pass


class IncorrectCommandException(Exception):  # Exception for incorrect command validation
    pass


class ExitCommandException(Exception):   # Exception for Exit command
    pass


class FinishInterpretationException(Exception):  # Exception to quit the App
    pass


class HandlerException(Exception):  # Exception for Handlers from Infrastructure layer
    pass
