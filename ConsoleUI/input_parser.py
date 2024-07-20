import console_commands as cm


def execute_user_input(u_input: list[str]):
    commands = {cm.AddBookCommand(),
                cm.RemoveBookCommand(),
                cm.FindBookCommand(),
                cm.ShowBooksCommand(),
                cm.ChangeBookStatusCommand()}
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
        raise Exception()
    pass
