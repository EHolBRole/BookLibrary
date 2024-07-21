import DDD.Application.application_api as a
import DDD.Application.application_dto as adto
import Exceptions.exceptions as ex


def premap_user_input(u_input: list[str]):
    if len(u_input) < 1:
        raise ex.IncorrectCommandException("Invalid input")

    request = adto.ApplicationDTORequest(u_input)

    return a.PreProcessRequest(request)
