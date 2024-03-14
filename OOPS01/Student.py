import unittest

"""
Create a class Student with following requirements
- Should have a data-member age
- Should have a data-member name
- Should support a constructor with both age and name
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TestStudent(unittest.TestCase):
    def test_init(self):
        person = Student("Alice", 25)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 25)

if __name__ == "__main__":
    unittest.main()