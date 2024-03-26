import concurrent.futures


def paint_quadrant(matrix, start_row, end_row, start_col, end_col, color):
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            matrix[i][j] = color


import concurrent.futures


def paint_quadrant(matrix, start_row, end_row, start_col, end_col, color):
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            matrix[i][j] = color


def divide_and_paint(matrix, colors):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []

        # Top-left quadrant
        futures.append(executor.submit(paint_quadrant, matrix, 0, len(matrix) // 2, 0, len(matrix[0]) // 2, colors[0]))

        # Top-right quadrant
        futures.append(executor.submit(paint_quadrant, matrix, 0, len(matrix) // 2, len(matrix[0]) // 2, len(matrix[0]),
                                       colors[1]))

        # Bottom-left quadrant
        futures.append(
            executor.submit(paint_quadrant, matrix, len(matrix) // 2, len(matrix), 0, len(matrix[0]) // 2, colors[2]))

        # Bottom-right quadrant
        futures.append(
            executor.submit(paint_quadrant, matrix, len(matrix) // 2, len(matrix), len(matrix[0]) // 2, len(matrix[0]),
                            colors[3]))

        for future in concurrent.futures.as_completed(futures):
            future.result()



# Example usage:
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# color is given
colors = ["red","blue","green","yellow"]

divide_and_paint(matrix, colors)

# Print the painted matrix
for row in matrix:
    print(row)

# Unit Tests
import unittest
from unittest.mock import patch
from concurrent.futures import ThreadPoolExecutor, wait


class TestDivideAndPaint(unittest.TestCase):
    # Pending : Write one more thread to test the executor
    def test_output_correctness(self):
        matrix = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        colors = ['red', 'blue', 'green', 'yellow']
        expected_output = [['red', 'red', 'blue', 'blue'],
                           ['red', 'red', 'blue', 'blue'],
                           ['green', 'green', 'yellow', 'yellow'],
                           ['green', 'green', 'yellow', 'yellow']]

        divide_and_paint(matrix, colors)

        # Check if the output matrix is painted correctly
        self.assertEqual(matrix, expected_output)


if __name__ == '__main__':
    unittest.main()