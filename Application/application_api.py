import Application.application_dto as ap
import Domain.domain_dto as d_dto
import Domain.domain_api as d_api
import Exceptions.exceptions as ex


def PreProcessRequest(request: ap.ApplicationDTORequest):
    is_executed = False
    for c in d_api.available_commands:
        if request.request_data[0] == c.name:
            request.request_data.pop(0)
            d_request = d_dto.DomainDTORequest(c, request.request_data)
            is_executed = True
            return d_api.ProcessRequest(d_request)
    if not is_executed:
        raise ex.IncorrectCommandException("Invalid command!")

    return False
