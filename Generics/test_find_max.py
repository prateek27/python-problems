import unittest
from find_max import find_max

class TestFindMax(unittest.TestCase):
    def test_find_max_int(self):
        int_list = [1, 5, 3, 7, 2]
        self.assertEqual(find_max(int_list), 7)

    def test_find_max_float(self):
        float_list = [2.5, 4.7, 3.2, 6.1, 5.0]
        self.assertEqual(find_max(float_list), 6.1)

    def test_find_max_empty_list(self):
        empty_list = []
        with self.assertRaises(ValueError):
            find_max(empty_list)

if __name__ == "__main__":
    unittest.main()