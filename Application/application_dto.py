class ApplicationDTORequest:  # DTO for request to Application layer
    def __init__(self, request_data: list):
        self.request_data = request_data
        pass
    pass


class ApplicationDTOResponse:  # DTO for response from Application layer
    def __init__(self, response_data: list):
        self.response_data = response_data
    pass
