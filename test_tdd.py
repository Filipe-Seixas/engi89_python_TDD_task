import unittest
import pytest

from code_tdd import Calculator


class CalcTest(unittest.TestCase):

    calc = Calculator()

    def test_remainder(self):
        self.assertEqual(self.calc.remainder(15, 3), 0)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(1, 5), 20.0)

    def test_is_positive(self):
        self.assertEqual(self.calc.is_positive(5), True)
