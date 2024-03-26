from abc import ABC, abstractmethod
import math

"""Implement an abstract class Shape in Python along with child classes like rectangle and circle.
Shape is an abstract class with abstract methods area() and perimeter().
Rectangle and Circle are child classes of Shape, implementing the area() and perimeter() methods specific to their shapes.
Rectangle takes length and width as parameters.
Circle takes radius as a parameter.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
rectangle = Rectangle(5, 4)
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 20
print("Rectangle perimeter:", rectangle.perimeter())  # Output: Rectangle perimeter: 18

circle = Circle(3)
print("Circle area:", circle.area())  # Output: Circle area: 28.274333882308138
print("Circle perimeter:", circle.perimeter())  # Output: Circle perimeter: 18.84955592153876

## Unit Tests
import unittest
import math

class TestShapes(unittest.TestCase):
    def test_rectangle(self):
        rectangle = Rectangle(5, 4)
        self.assertEqual(rectangle.area(), 20)
        self.assertEqual(rectangle.perimeter(), 18)

    def test_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 3 ** 2, delta=0.0001)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * 3, delta=0.0001)

if __name__ == '__main__':
    unittest.main()