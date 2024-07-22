import Domain.commands as c


class DomainDTORequest:  # Request to Domain Layer
    def __init__(self, command: c.Command, args: list):
        self.command = command
        self.args = args
        pass

    pass


class DomainDTOResponse:  # Response from Domain Layer
    def __init__(self, response_data: list, status: bool):
        self.response_data = response_data
        self.status = status
        pass

    pass
