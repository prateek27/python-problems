"""We define a Person class with attributes name and age.
We implement the find_unique_persons function, which takes a list of Person objects as input and returns a list containing only the unique persons based on their names.
We demonstrate the usage of the find_unique_persons function with an example list of Person objects.
This function ensures that only the first occurrence of each name is included in the output list, making the list contain unique persons based on their names.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def find_unique_persons(people):
    #todo
    unique_names = set()
    unique_persons = []
    for person in people:
        if person.name not in unique_names:
            unique_names.add(person.name)
            unique_persons.append(person)
    return unique_persons

# Example usage:
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 35)
person4 = Person("Charlie", 40)

people = [person1, person2, person3, person4]

unique_persons = find_unique_persons(people)
for person in unique_persons:
    print(f"Name: {person.name}, Age: {person.age}")