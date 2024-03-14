import copy
import unittest
import Point
# in this example, the Rectangle class has a single constructor that
# accepts variable-length arguments *args.
# Depending on the number and types of arguments provided,
# it initializes the topLeft and bottomRight attributes accordingly.
# This allows for different ways of creating Rectangle objects without having
# separate constructor methods

"Make sure you do the imports"
Point = Point.Point

class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            # If two Point objects are provided, initialize from points
            self.topLeft = copy.deepcopy(args[0])
            self.bottomRight = copy.deepcopy(args[1])
        elif len(args) == 4:
            # If four integer coordinates are provided, initialize from coordinates
            self.topLeft = Point(args[0], args[1])
            self.bottomRight = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], Rectangle):
            # If a Rectangle object is provided, initialize by copying
            self.topLeft = copy.deepcopy(args[0].topLeft)
            self.bottomRight = copy.deepcopy(args[0].bottomRight)
        else:
            raise ValueError("Invalid arguments provided.")


class TestRectangle(unittest.TestCase):
    def test_constructor_with_coordinates(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.topLeft.x, 1)
        self.assertEqual(rectangle.topLeft.y, 2)
        self.assertEqual(rectangle.bottomRight.x, 3)
        self.assertEqual(rectangle.bottomRight.y, 4)

    def test_constructor_with_points(self):
        topLeft = Point(1, 2)
        bottomRight = Point(3, 4)
        rectangle = Rectangle(topLeft, bottomRight)
        self.assertEqual(rectangle.topLeft, topLeft)
        self.assertEqual(rectangle.bottomRight, bottomRight)
        self.assertIsNot(rectangle.topLeft, topLeft)
        # self.assertIsNot(rectangle.bottomRight, bottomRight)

    def test_constructor_with_rectangle(self):
        originalRectangle = Rectangle(1, 2, 3, 4)
        copiedRectangle = Rectangle(originalRectangle)
        self.assertEqual(originalRectangle.topLeft, copiedRectangle.topLeft)
        self.assertEqual(originalRectangle.bottomRight, copiedRectangle.bottomRight)
        self.assertIsNot(originalRectangle.topLeft, copiedRectangle.topLeft)
        self.assertIsNot(originalRectangle.bottomRight, copiedRectangle.bottomRight)


if __name__ == "__main__":
    unittest.main()
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(Point(1, 2), Point(3, 4))
    rect3 = Rectangle(rect1)
# Usage:
