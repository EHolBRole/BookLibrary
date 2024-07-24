import unittest
import unittest.mock
import Application.application_dto as a_dto
import Application.application_api as a_api
import api_library as al
import Tests.test_init as i


class TestApplicationAPI(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        i.test_init()
        super().__init__(*args, **kwargs)

    def test_pre_process_request(self):
        test_input1 = ['add', 'test', 'test', '2000']
        test_input2 = ['ls']
        test_input3 = ['rm', '1']

        expected_response2 = a_dto.ApplicationDTOResponse([{'author': 'test', 'status': 'stocked', 'title': 'test', 'year': '2000', 'id': 1}])

        request1 = a_dto.ApplicationDTORequest(test_input1)
        request2 = a_dto.ApplicationDTORequest(test_input2)
        request3 = a_dto.ApplicationDTORequest(test_input3)

        response1 = a_api.pre_process_request(request1)
        response2 = a_api.pre_process_request(request2)
        response3 = a_api.pre_process_request(request3)

        self.assertEqual(response1.response_data, [])
        self.assertEqual(response2.response_data, expected_response2.response_data)
        self.assertEqual(response3.response_data, [])
        pass

    pass
