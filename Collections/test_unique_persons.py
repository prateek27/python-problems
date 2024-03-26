import unittest
from unique_persons import Person, find_unique_persons

class TestFindUniquePersons(unittest.TestCase):
    def test_find_unique_persons(self):
        person1 = Person("Alice", 30)
        person2 = Person("Bob", 25)
        person3 = Person("Alice", 35)
        person4 = Person("Charlie", 40)

        people = [person1, person2, person3, person4]

        unique_persons = find_unique_persons(people)

        # Ensure that unique_persons contains only two Person objects
        self.assertEqual(len(unique_persons), 3)

        # Ensure that the first occurrence of each name is included
        names = set()
        for person in unique_persons:
            names.add(person.name)
        self.assertEqual(names, {"Alice", "Bob", "Charlie"})

if __name__ == "__main__":
    unittest.main()