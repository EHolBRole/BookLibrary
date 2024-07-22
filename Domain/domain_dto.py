import Domain.commands as c


class DomainDTORequest:
    def __init__(self, command: c.Command, args: list):
        self.command = command
        self.args = args
        pass

    pass


class DomainDTOResponse:
    def __init__(self, response_data: list, status: bool):
        self.response_data = response_data
        self.status = status
        pass

    pass
