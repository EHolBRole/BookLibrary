import DDD.Application.application_api as a
import Exceptions.exceptions as ex


def premap_user_input(u_input: list[str]):
    if len(u_input) < 1:
        raise ex.IncorrectCommandException("Invalid input")

    a.PreProcessData(u_input)
    pass
