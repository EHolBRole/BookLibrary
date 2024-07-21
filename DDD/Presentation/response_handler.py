import DDD.Application.application_dto as a_dto


def process_response(response: a_dto.ApplicationDTOResponse):
    print(response.response_data)
    pass
