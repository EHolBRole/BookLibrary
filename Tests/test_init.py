import api_library as al
import Infrastructure.handlers as h
import Infrastructure.infrastructure_api as i_api


def test_init():
    al.LibraryAPI.infrastructure_api = i_api.InfrastructureAPI(h.JsonHandler('../../JSON/library.json'))
    pass
