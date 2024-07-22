import unittest
import Application.application_dto as a_dto
import Presentation.library as ll
import io
import builtins

from unittest import mock


class TestLibraryLaunch(unittest.TestCase):
    def test_get_input(self):
        with mock.patch.object(builtins, 'input', lambda: 'rm 1'):
            output = ll.get_input()
            self.assertEqual(output, ['rm', '1'])
        pass
    pass
