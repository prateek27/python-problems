# Unit Tests
import unittest
from unittest.mock import patch, MagicMock
import random
from quicksort import quicksort

class TestQuickSort(unittest.TestCase):
    @patch('quicksort.concurrent.futures.ThreadPoolExecutor.submit')
    def test_empty_array(self, mock_submit):
        arr = []
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [])
        # Ensure that ThreadPoolExecutor.submit was not called
        mock_submit.assert_not_called()

    @patch('quicksort.concurrent.futures.ThreadPoolExecutor.submit')
    def test_single_element_array(self, mock_submit):
        arr = [5]
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [5])
        # Ensure that ThreadPoolExecutor.submit was not called
        mock_submit.assert_not_called()

    @patch('quicksort.concurrent.futures.ThreadPoolExecutor.submit')
    def test_sorted_array(self, mock_submit):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = quicksort(arr)
        # Ensure that ThreadPoolExecutor.submit was called
        mock_submit.assert_called()

    def test_empty_array_values(self):
        arr = []
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [])

    def test_single_element_array_values(self):
        arr = [5]
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [5])

    def test_sorted_array_values(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array_values(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_random_array_values(self):
        arr = random.sample(range(1, 100), 20)
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, sorted(arr))


if __name__ == '__main__':
    unittest.main()