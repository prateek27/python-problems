import unittest
from compare import compare

class TestCompare(unittest.TestCase):
    def test_direct_comparison(self):
        self.assertEqual(compare(5, 10), -1)
        self.assertEqual(compare("abc", "abc"), 0)
        self.assertEqual(compare(20, 10), 1)

    def test_comparison_with_key_function(self):
        students = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
            {"name": "Charlie", "age": 20}
        ]

        # Sort students by age
        sorted_students = sorted(students, key=lambda x: x['age'])

        expected_result = [
            {"name": "Charlie", "age": 20},
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30}
        ]

        self.assertEqual(sorted_students, expected_result)

if __name__ == "__main__":
    unittest.main()