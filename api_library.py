import Infrastructure.handler_enum as he
import Infrastructure.infrastructure_api as i_api


class LibraryRepository:  # Repository for all the necessary implementations of classes
    infrastructure_api = None
    pass


def init():  # Initializes Library Repository
    LibraryRepository.infrastructure_api = i_api.get_api(he.Handlers.JSON)
    pass
