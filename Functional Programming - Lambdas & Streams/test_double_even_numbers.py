import unittest
from double_even_numbers import filter_and_double_even_numbers


class TestFilterAndDoubleEvenNumbersTestCase(unittest.TestCase):
    def test_filter_and_double_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6]
        expected_result = [4, 8, 12]
        self.assertEqual(filter_and_double_even_numbers(numbers), expected_result)

    def test_empty_list(self):
        numbers = []
        self.assertEqual(filter_and_double_even_numbers(numbers), [])

    def test_no_even_numbers(self):
        numbers = [1, 3, 5]
        self.assertEqual(filter_and_double_even_numbers(numbers), [])

    def test_all_even_numbers(self):
        numbers = [2, 4, 6, 8]
        expected_result = [4, 8, 12, 16]
        self.assertEqual(filter_and_double_even_numbers(numbers), expected_result)


if __name__ == "__main__":
    unittest.main()