import Application.application_dto as a_dto
import Domain.domain_dto as d_dto
import Domain.domain_api as d_api
import Exceptions.exceptions as ex


def PreProcessRequest(request: a_dto.ApplicationDTORequest):
    is_executed = False
    for c in d_api.available_commands:
        if request.request_data[0] == c.name:
            request.request_data.pop(0)
            d_request = d_dto.DomainDTORequest(c, request.request_data)
            is_executed = True
            domain_response = d_api.ProcessRequest(d_request)
            return a_dto.ApplicationDTOResponse(domain_response.response_data)
    if not is_executed:
        raise ex.IncorrectCommandException("Invalid command!")

    return False
