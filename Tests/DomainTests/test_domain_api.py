import unittest
import unittest.mock
import Domain.domain_dto as d_dto
import Domain.domain_api as d_api
import api_library as al
import Tests.test_init as i


class TestInputMapper(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        i.test_init()
        super().__init__(*args, **kwargs)

    def test_premap_user_input(self):
        test_input1 = ['add', 'test', 'test', '2000']
        test_input2 = ['ls']
        test_input3 = ['rm', '1']

        expected_response2 = d_dto.DomainDTORequest([{'author': 'test', 'status': 'stocked', 'title': 'test', 'year': '2000'}])

        request1 = d_dto.DomainDTORequest(test_input1)
        request2 = d_dto.DomainDTORequest(test_input2)
        request3 = d_dto.DomainDTORequest(test_input3)

        response1 = d_api.ProcessRequest(request1)
        response2 = d_api.ProcessRequest(request2)
        response3 = d_api.ProcessRequest(request3)

        self.assertEqual(response1, True)
        self.assertEqual(response2.response_data, expected_response2.args)
        self.assertEqual(response3, True)
        pass

    pass
