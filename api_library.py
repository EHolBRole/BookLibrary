import Infrastructure.handler_enum as he
import Infrastructure.infrastructure_api as i_api


class LibraryAPI:
    infrastructure_api = None
    pass


def init():
    LibraryAPI.infrastructure_api = i_api.get_api(he.Handlers.JSON)
    pass
