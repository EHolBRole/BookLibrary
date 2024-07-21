import DDD.Application.application_dto as a_dto


def process_response(response: a_dto.ApplicationDTOResponse):
    for el in response.response_data:
        print(el)
    pass
