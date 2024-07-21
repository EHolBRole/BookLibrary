import Application.application_api as a
import Application.application_dto as a_dto
import Exceptions.exceptions as ex


def premap_user_input(u_input: list[str]):
    if len(u_input) < 1:
        raise ex.IncorrectCommandException("Invalid input")

    request = a_dto.ApplicationDTORequest(u_input)

    return a.PreProcessRequest(request)
