import console_commands as cm
import Exceptions.exceptions as ex


def execute_user_input(u_input: list[str]):
    commands = {cm.AddBookCommand('../JSON/library.json'),
                cm.RemoveBookCommand('../JSON/library.json'),
                cm.FindBookCommand('../JSON/library.json'),
                cm.ShowBooksCommand('../JSON/library.json'),
                cm.ChangeBookStatusCommand('../JSON/library.json'),
                cm.ExitAppCommand('../JSON/library.json')}
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
