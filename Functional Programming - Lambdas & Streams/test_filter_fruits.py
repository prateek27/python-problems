import unittest
from filter_fruits import filter_fruits_starting_with_a


class TestFilterFruitsStartingWithATestCase(unittest.TestCase):
    def test_filter_fruits_starting_with_a(self):
        fruits = ["apple", "banana", "avocado", "orange", "apricot"]
        expected_result = ['apple', 'avocado', 'apricot']
        self.assertEqual(filter_fruits_starting_with_a(fruits), expected_result)

    def test_empty_list(self):
        fruits = []
        self.assertEqual(filter_fruits_starting_with_a(fruits), [])

    def test_no_fruits_starting_with_a(self):
        fruits = ["banana", "orange"]
        self.assertEqual(filter_fruits_starting_with_a(fruits), [])

    def test_all_fruits_starting_with_a(self):
        fruits = ["apple", "avocado", "apricot"]
        self.assertEqual(filter_fruits_starting_with_a(fruits), fruits)


if __name__ == "__main__":
    unittest.main()