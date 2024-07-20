import console_commands as cm


def parse_user_input(u_input: list[str]):

    commands = {cm.AddBookCommand(),
                cm.RemoveBookCommand(),
                cm.FindBookCommand(),
                cm.ShowBooksCommand(),
                cm.ChangeBookStatusCommand()}

    for c in commands:
        if c.name == u_input[0]:
            u_input.pop(0)
            c.execute()
    raise Exception()
    pass
