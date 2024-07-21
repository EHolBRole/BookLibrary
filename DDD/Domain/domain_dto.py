import commands


class DomainDTORequest:
    def __init__(self, command: commands.Command, args: list):
        self.command = command
        self.args = args
        pass
    pass


class DomainDTOResponse:
    pass
