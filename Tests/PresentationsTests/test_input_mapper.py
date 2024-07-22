import unittest
import unittest.mock
import Application.application_dto as a_dto
import Presentation.input_mapper as im
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

        response1 = im.premap_user_input(test_input1)
        response2 = im.premap_user_input(test_input2)
        response3 = im.premap_user_input(test_input3)

        self.assertEqual(response1, True)
        self.assertEqual(response2, True)
        self.assertEqual(response3, True)
        pass

    pass
