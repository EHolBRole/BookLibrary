import unittest
import unittest.mock
import Domain.domain_dto as d_dto
import Domain.domain_api as d_api
import Domain.commands as c
import api_library as al
import Tests.test_init as i


class Test1AddCommand(unittest.TestCase):
    def test_add_is_user_input_valid(self):
        i.test_init()
        test_input1 = ['test', 'test', '2000']
        add_c = c.AddBookCommand()

        response = add_c.is_user_input_valid(test_input1)

        self.assertEqual(response, True)
        pass

    def test_add_execute(self):
        i.test_init()
        test_input1 = ['test', 'test', '2000']
        add_c = c.AddBookCommand()
        expected_response = d_dto.DomainDTOResponse([], True)

        response = add_c.execute(test_input1)

        self.assertEqual(response.response_data, expected_response.response_data)
        self.assertEqual(response.status, expected_response.status)
        pass
    pass


class Test3ShowCommand(unittest.TestCase):

    def test_show_is_user_input_valid(self):
        i.test_init_test_lib()
        test_input1 = []
        test_input2 = ['something']
        show_c = c.ShowBooksCommand()

        response1 = show_c.is_user_input_valid(test_input1)
        response2 = show_c.is_user_input_valid(test_input2)

        self.assertEqual(response1, True)
        self.assertEqual(response2, False)
        pass

    def test_show_execute(self):
        i.test_init_test_lib()
        test_input1 = []
        show_c = c.ShowBooksCommand()
        expected_response = d_dto.DomainDTOResponse([{"title": "test", "author": "test", "year": "2000", "status": "stocked"}], True)

        response = show_c.execute(test_input1)

        self.assertEqual(expected_response.response_data, response.response_data)
        self.assertEqual(response.status, expected_response.status)
        pass
    pass


class Test4FindCommand(unittest.TestCase):

    def test_find_is_user_input_valid(self):
        i.test_init_test_lib()
        test_input1 = ['test']
        test_input2 = ['something', 'something']
        find_c = c.FindBookCommand()

        response1 = find_c.is_user_input_valid(test_input1)
        response2 = find_c.is_user_input_valid(test_input2)

        self.assertEqual(response1, True)
        self.assertEqual(response2, False)
        pass

    def test_find_execute(self):
        i.test_init_test_lib()
        test_input1 = ['test']
        find_c = c.FindBookCommand()
        expected_response = d_dto.DomainDTOResponse([{"title": "test", "author": "test", "year": "2000", "status": "stocked"}], True)

        response = find_c.execute(test_input1)

        self.assertEqual(expected_response.response_data, response.response_data)
        self.assertEqual(response.status, expected_response.status)
        pass
    pass


class Test5StatusChangeCommand(unittest.TestCase):

    def test_status_change_is_user_input_valid(self):
        i.test_init_test_lib()
        test_input1 = ['1', 'given']
        test_input2 = ['something', 'something']
        test_input3 = ['something']
        schange_c = c.ChangeBookStatusCommand()

        response1 = schange_c.is_user_input_valid(test_input1)
        response2 = schange_c.is_user_input_valid(test_input2)
        response3 = schange_c.is_user_input_valid(test_input3)

        self.assertEqual(response1, True)
        self.assertEqual(response2, False)
        self.assertEqual(response3, False)
        pass

    def test_status_change_execute(self):
        i.test_init_test_lib()
        test_input1 = ['2', 'given']
        test_input2 = ['2', 'stocked']
        schange_c = c.ChangeBookStatusCommand()
        expected_response1 = d_dto.DomainDTOResponse([], True)
        expected_response2 = d_dto.DomainDTOResponse([], True)

        response1 = schange_c.execute(test_input1)
        response2 = schange_c.execute(test_input2)

        self.assertEqual(expected_response1.response_data, response1.response_data)
        self.assertEqual(expected_response2.response_data, response2.response_data)
        self.assertEqual(response1.status, expected_response1.status)
        self.assertEqual(response2.status, expected_response2.status)
        pass

    pass


class Test2RemoveCommand(unittest.TestCase):
    def test_remove_is_user_input_valid(self):
        i.test_init()
        test_input1 = ['1']
        test_input2 = ['something']
        add_c = c.RemoveBookCommand()

        response1 = add_c.is_user_input_valid(test_input1)
        response2 = add_c.is_user_input_valid(test_input2)

        self.assertEqual(response1, True)
        self.assertEqual(response2, False)
        pass

    def test_remove_execute(self):
        i.test_init()
        test_input1 = ['1']
        add_c = c.RemoveBookCommand()
        expected_response = d_dto.DomainDTOResponse([], True)

        response = add_c.execute(test_input1)

        self.assertEqual(response.response_data, expected_response.response_data)
        self.assertEqual(response.status, expected_response.status)
        pass
    pass
