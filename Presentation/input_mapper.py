import Application.application_api as a
import Application.application_dto as a_dto
import Exceptions.exceptions as ex
import Presentation.response_handler as rh


def premap_user_input(u_input: list[str]):
    if len(u_input) < 1:
        raise ex.IncorrectCommandException("Invalid input")

    request = a_dto.ApplicationDTORequest(u_input)
    response = a.PreProcessRequest(request)

    if type(response) is not bool:
        rh.process_response(response)
        return True
    else:
        return response
