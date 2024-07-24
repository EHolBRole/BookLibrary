import unittest
import unittest.mock
import Domain.domain_dto as d_dto
import Domain.domain_api as d_api
import Domain.commands as c
import api_library as al
import Tests.test_init as i


class Test6DomainAPI(unittest.TestCase):
    def test_process_request(self):
        i.test_init()
        test_command1 = c.AddBookCommand()
        test_command2 = c.ShowBooksCommand()
        test_command3 = c.RemoveBookCommand()
        test_input1 = ['test', 'test', '2000']
        test_input2 = []
        test_input3 = ['1']

        expected_response2 = d_dto.DomainDTOResponse([{"title": "test", "author": "test", "year": "2000", "status": "stocked", "id": 1}], True)

        request1 = d_dto.DomainDTORequest(test_command1, test_input1)
        request2 = d_dto.DomainDTORequest(test_command2, test_input2)
        request3 = d_dto.DomainDTORequest(test_command3, test_input3)

        response1 = d_api.process_request(request1)
        response2 = d_api.process_request(request2)
        response3 = d_api.process_request(request3)

        self.assertEqual(response1.status, True)
        self.assertEqual(response2.response_data, expected_response2.response_data)
        self.assertEqual(response3.status, True)
        pass

    pass
