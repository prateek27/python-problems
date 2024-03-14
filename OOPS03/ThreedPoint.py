import unittest

import unittest
import io
from unittest.mock import patch

"""Note: Use F-strings in the display method. They provide a concise and readable way to create formatted strings in Python, 
introduced in Python 3.6. They are more efficient and easier to read compared to older methods of 
string formatting like % formatting or str.format()."""

"Point class is already given to you"
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(f"[{self._x}, {self._y}]")


"""Todo for the learner"""
class ThreedPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def display(self):
        print(f"[{self._x}, {self._y}, {self.__z}]")


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(2, 3)  # Sample Point

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.point.display()
            self.assertEqual(mock_stdout.getvalue(), "[2, 3]\n")


class TestThreedPoint(unittest.TestCase):
    def setUp(self):
        self.threed_point = ThreedPoint(2, 3, 4)  # Sample ThreedPoint

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.threed_point.display()
            self.assertEqual(mock_stdout.getvalue(), "[2, 3, 4]\n")


if __name__ == '__main__':
    unittest.main()