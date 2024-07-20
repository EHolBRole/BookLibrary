import unittest
import Exceptions.exceptions as ex
import ConsoleUI.console_commands as cc


class ExitAppCommandTestCase(unittest.TestCase):

    def test_is_user_input_valid(self):
        ea_command = cc.ExitAppCommand('../JSON/library.json')
        args = []

        flag = ea_command.is_user_input_valid(args)

        self.assertEqual(True, flag)

    def test_correct_execute(self):
        ea_command = cc.ExitAppCommand('../JSON/library.json')
        args = []
        with self.assertRaises(ex.FinishInterpretationException):
            ea_command.execute(args)

    def test_incorrect_execute(self):
        ea_command = cc.ExitAppCommand('../JSON/library.json')
        args = ['test', 'test']
        with self.assertRaises(ex.ExitCommandException):
            ea_command.execute(args)

    pass
