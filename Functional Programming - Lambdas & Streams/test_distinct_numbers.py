import unittest
from distinct_numbers import getDistinctNumbers

class TestGetDistinctNumbersTestCase(unittest.TestCase):
    def test_get_distinct_numbers(self):
        numbers = [1, 2, 3, 4, 4, 5, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(getDistinctNumbers(numbers), expected_result)

    def test_empty_list(self):
        numbers = []
        self.assertEqual(getDistinctNumbers(numbers), [])

    def test_single_element_list(self):
        numbers = [1]
        self.assertEqual(getDistinctNumbers(numbers), [1])

    def test_all_duplicates(self):
        numbers = [2, 2, 2, 2]
        self.assertEqual(getDistinctNumbers(numbers), [2])


if __name__ == "__main__":
    unittest.main()
