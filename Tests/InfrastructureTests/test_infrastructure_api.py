import unittest
import unittest.mock
import Domain.domain_dto as d_dto
import Domain.domain_api as d_api
import Infrastructure.infrastructure_api as i_api
import Infrastructure.handler_enum as he
import Infrastructure.handlers as h
import Domain.commands as c
import api_library as al
import Tests.test_init as i


class TestInfrastructureAPI(unittest.TestCase):

    def test_get_api(self):
        i.test_init()
        expected_result = i_api.InfrastructureAPI(h.JsonHandler('JSON/library.json'))

        result = i_api.get_api(he.Handlers.JSON)

        self.assertEqual(type(expected_result.handler), type(result.handler))

        pass

    def test_get_data(self):
        i.test_init()
        expected_result = {}

        result = al.LibraryAPI.infrastructure_api.get_data()

        self.assertEqual(expected_result, result)
        pass

    def test_push_data(self):
        i.test_init()
        expected_result = {}

        al.LibraryAPI.infrastructure_api.push_data({})

        result = al.LibraryAPI.infrastructure_api.get_data()

        self.assertEqual(expected_result, result)
        pass
    pass
