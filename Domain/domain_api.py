import Domain.commands as cm
import Domain.domain_dto as d_dto

"""
This module is for communication to Domain from other layers
"""


def process_request(request: d_dto.DomainDTORequest):  # Processes request to Domain.
    return request.command.execute(request.args)
    pass


# list of all available commands
available_commands = {cm.AddBookCommand(),
                      cm.ShowBooksCommand(),
                      cm.RemoveBookCommand(),
                      cm.FindBookCommand(),
                      cm.ChangeBookStatusCommand(),
                      cm.ExitAppCommand()}

