import api_library as al
import Infrastructure.handlers as h
import Infrastructure.infrastructure_api as i_api


def test_init():
    al.LibraryRepository.infrastructure_api = i_api.InfrastructureAPI(h.JsonHandler('/home/eholbrole/Work/TestTasks/EffectiveMobile/Tests/TestJSON/library.json'))
    pass


def test_init_test_lib():
    al.LibraryRepository.infrastructure_api = i_api.InfrastructureAPI(h.JsonHandler('/home/eholbrole/Work/TestTasks/EffectiveMobile/Tests/TestJSON/test_library.json'))
    pass
