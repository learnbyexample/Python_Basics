#!/usr/bin/python3

import palindrome
import unittest
from unittest import mock
from io import StringIO

class TestPalindrome(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def main_op(self, tst_str, mock_stdout):
        with mock.patch('builtins.input', side_effect=tst_str):
            palindrome.main()
        return mock_stdout.getvalue()

    def test_valid(self):
        for s in ('Malayalam', 'kek'):
            self.assertEqual(self.main_op([s]), s + ' is a palindrome\n')

        for s in ('zzz', 'cool'):
            self.assertEqual(self.main_op([s]), s + ' is NOT a palindrome\n')

    def test_error(self):
        em1 = 'Error: Characters other than alphabets and punctuations\n'
        em2 = 'Error: Less than 3 alphabets\n'

        tst1 = em1 + 'Madam is a palindrome\n'
        self.assertEqual(self.main_op(['123', 'Madam']), tst1)

        tst2 = em2 + em1 + 'Jerry is NOT a palindrome\n'
        self.assertEqual(self.main_op(['to', 'a2a', 'Jerry']), tst2)

if __name__ == '__main__':
    unittest.main()
