import Domain.commands as c


class DomainDTORequest:
    def __init__(self, command: c.Command, args: list):
        self.command = command
        self.args = args
        pass
    pass

