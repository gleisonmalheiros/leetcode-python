from unittest import TestCase
from easy.valid_parentheses import ValidParentheses


class TestValidParentheses(TestCase):
    def test_is_valid1(self):
        actual = ValidParentheses.isValid('()')
        expected = True
        self.assertEqual(expected, actual)

    def test_is_valid2(self):
        actual = ValidParentheses.isValid('()[]{}')
        expected = True
        self.assertEqual(expected, actual)

    def test_is_valid3(self):
        actual = ValidParentheses.isValid('[(()[]{})]')
        expected = True
        self.assertEqual(expected, actual)

    def test_is_valid4(self):
        actual = ValidParentheses.isValid('(]')
        expected = False
        self.assertEqual(expected, actual)

    def test_is_valid5(self):
        actual = ValidParentheses.isValid(']')
        expected = False
        self.assertEqual(expected, actual)

    def test_is_valid6(self):
        actual = ValidParentheses.isValid('{)')
        expected = False
        self.assertEqual(expected, actual)

    def test_is_valid7(self):
        actual = ValidParentheses.isValid('(}')
        expected = False
        self.assertEqual(expected, actual)

    def test_is_valid8(self):
        actual = ValidParentheses.isValid('(A')
        expected = False
        self.assertEqual(expected, actual)
