import unittest
import unittest.mock
import Application.application_dto as a_dto
import Presentation.response_handler as rh
import io
import Tests.test_init as i


class TestResponseHandler(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        i.test_init()
        super().__init__(*args, **kwargs)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_process_response(self, mock_stdout):
        response = a_dto.ApplicationDTOResponse(['test', 'test'])
        rh.process_response(response)
        self.assertEqual(mock_stdout.getvalue(), 'test\ntest\n')
        pass
    pass
