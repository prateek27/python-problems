import unittest
from divide_by_zero import *

class TestDivideNumbersTestCase(unittest.TestCase):
    def test_divide_by_zero(self):
        # When dividing by zero, it should raise a DivisionByZeroError
        with self.assertRaises(DivisionByZeroError):
            divide_numbers(10, 0)

    def test_divide_by_non_zero(self):
        # When dividing by a non-zero number, it should return the result
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_divide_zero_by_non_zero(self):
        # When dividing zero by a non-zero number, it should return zero
        result = divide_numbers(0, 5)
        self.assertEqual(result, 0)

    def test_divide_zero_by_zero(self):
        # When dividing zero by zero, it should raise a DivisionByZeroError
        with self.assertRaises(DivisionByZeroError):
            divide_numbers(0, 0)


if __name__ == "__main__":
    unittest.main()