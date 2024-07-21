import commands as cm


def ProcessRequest(request):
    pass


available_commands = {cm.AddBookCommand(),
                      cm.ShowBooksCommand(),
                      cm.RemoveBookCommand(),
                      cm.FindBookCommand(),
                      cm.ChangeBookStatusCommand(),
                      cm.ExitAppCommand()}

