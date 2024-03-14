import unittest


# Implement a Person class that allows constructing objects with a variable number of parameters
# using *args. The constructor should initialize the name attribute for
# all objects and optionally the age attribute if provided.
# raise IndexError() if number of arguments is more than 2 or zero

class Person:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            raise IndexError()

import unittest

class TestPerson(unittest.TestCase):
    def test_constructor_with_name_only(self):
        person = Person("Alice")
        self.assertEqual(person.name, "Alice")
        self.assertFalse(hasattr(person, 'age'))

    def test_constructor_with_name_and_age(self):
        person = Person("Bob", 30)
        self.assertEqual(person.name, "Bob")
        self.assertEqual(person.age, 30)

    def test_constructor_with_no_arguments(self):
        with self.assertRaises(IndexError):
            person = Person()

    def test_constructor_with_too_many_arguments(self):
        with self.assertRaises(IndexError):
            person = Person("Alice", 25, "USA")

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()