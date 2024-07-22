import unittest
import Application.application_dto as a_dto
import Presentation.library as ll
import Tests.test_init as i
import builtins

from unittest import mock


class TestLibraryLaunch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        i.test_init()
        super().__init__(*args, **kwargs)

    def test_get_input(self):
        with mock.patch.object(builtins, 'input', lambda: 'rm 1'):
            output = ll.get_input()
            self.assertEqual(output, ['rm', '1'])
        pass
    pass
