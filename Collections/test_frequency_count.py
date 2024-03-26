import unittest
from frequency_count import count_frequency

class TestCountFrequency(unittest.TestCase):
    def test_count_frequency(self):
        arr = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
        expected_frequency = {1: 4, 2: 3, 3: 2, 4: 1}
        self.assertEqual(count_frequency(arr), expected_frequency)

    def test_count_frequency_empty_array(self):
        arr = []
        expected_frequency = {}
        self.assertEqual(count_frequency(arr), expected_frequency)

    def test_count_frequency_single_element_array(self):
        arr = [5]
        expected_frequency = {5: 1}
        self.assertEqual(count_frequency(arr), expected_frequency)

if __name__ == "__main__":
    unittest.main()