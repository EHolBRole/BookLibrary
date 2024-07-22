import unittest
import unittest.mock
import Application.application_dto as a_dto
import Presentation.response_handler as rh
import io


class TestResponseHandler(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_process_response(self, mock_stdout):
        response = a_dto.ApplicationDTOResponse(['test', 'test'])
        rh.process_response(response)
        self.assertEqual(mock_stdout.getvalue(), 'test\ntest\n')
        pass
    pass
