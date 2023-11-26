import unittest
from easy.roman_to_integer import RomanToInteger


class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(3, RomanToInteger.roman_to_int('III'))
        self.assertEqual(58, RomanToInteger.roman_to_int('LVIII'))
        self.assertEqual(1994, RomanToInteger.roman_to_int('MCMXCIV'))
        self.assertEqual(666, RomanToInteger.roman_to_int('DCLXVI'))
        self.assertEqual(999, RomanToInteger.roman_to_int('CMXCIX'))
        self.assertEqual(831, RomanToInteger.roman_to_int('DCCCXXXI'))
