import copy
import unittest

"single constructor, copy and deep copy to be tested"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __copy__(self):
        # Create a new instance of Point with the same coordinates
        return Point(self.x, self.y)

    def __deepcopy__(self, memo):
        # Create a new instance of Point with deep copies of coordinates
        return Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))


class TestPoint(unittest.TestCase):
    def test_constructor(self):
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_copy(self):
        point = Point(3, 4)
        point_copy = copy.copy(point)
        self.assertEqual(point, point_copy)
        self.assertIsNot(point, point_copy)

    def test_deepcopy(self):
        point = Point(3, 4)
        point_deepcopy = copy.deepcopy(point)
        self.assertEqual(point, point_deepcopy)
        self.assertIsNot(point, point_deepcopy)


if __name__ == "__main__":
    unittest.main()
