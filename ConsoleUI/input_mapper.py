import DDD.Domain.commands as cm
import Exceptions.exceptions as ex


def execute_user_input(u_input: list[str]):
    address = '../../JSON/library.json'
    commands = {cm.AddBookCommand(address),
                cm.RemoveBookCommand(address),
                cm.FindBookCommand(address),
                cm.ShowBooksCommand(address),
                cm.ChangeBookStatusCommand(address),
                cm.ExitAppCommand(address)}
    if len(u_input) < 1:
        raise Exception()
    is_executed = False
    for c in commands:
        if c.name == u_input[0]:
            u_input.pop(0)
            c.execute(u_input)
            is_executed = True
            break
    if not is_executed:
        raise ex.IncorrectCommandException("Command not found")
    pass
