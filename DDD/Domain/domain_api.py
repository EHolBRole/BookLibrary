import commands as cm
import domain_dto as d_dto


def ProcessRequest(request: d_dto.DomainDTORequest):
    return request.command.execute(request.args)
    pass


available_commands = {cm.AddBookCommand(),
                      cm.ShowBooksCommand(),
                      cm.RemoveBookCommand(),
                      cm.FindBookCommand(),
                      cm.ChangeBookStatusCommand(),
                      cm.ExitAppCommand()}

