import unittest
import ConsoleUI.console_commands as cc
import json

from Library.library_model import Book


class AddBookCommandTestCase(unittest.TestCase):

    def test_is_user_input_valid(self):
        ab_command = cc.AddBookCommand('../JSON/library.json')
        args = ['test', 'test2', 'test3']

        flag = ab_command.is_user_input_valid(args)

        self.assertEqual(True, flag)

    def test_correct_execute(self):
        ab_command = cc.AddBookCommand('JsonTest/library.json')
        args1 = ['test1', 'test2', '2000']
        args2 = ['test1', 'test2', '2001']
        args3 = ['test1', 'test2', '2002']

        ab_command.execute(args1)
        ab_command.execute(args2)
        ab_command.execute(args3)

        with open('JsonTest/test.json', 'r') as f1:
            with open('JsonTest/library.json', 'r+') as f2:
                self.assertEqual(json.load(f1), json.load(f2))
                f2.truncate(0)

    def test_parse_book_to_json(self):
        ab_command = cc.AddBookCommand('JsonTest/library.json')
        b1 = Book('test1', 'test2', '2000')
        b2 = Book('test1', 'test2', '2001')
        b3 = Book('test1', 'test2', '2002')

        ab_command.parse_book_to_json(b1)
        ab_command.parse_book_to_json(b2)
        ab_command.parse_book_to_json(b3)

        with open('JsonTest/test.json', 'r') as f1:
            with open('JsonTest/library.json', 'r+') as f2:
                self.assertEqual(json.load(f1), json.load(f2))
                f2.truncate(0)
    pass
