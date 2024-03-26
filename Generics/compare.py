"""We define a generic compare function that takes two objects x and y of the same type and an optional key function key that extracts a comparable key from each object.
If key is provided, it compares the keys extracted from x and y. Otherwise, it directly compares x and y.
The function returns -1 if x < y, 0 if x == y, and 1 if x > y.
We demonstrate the usage of the compare function with examples of direct comparison and comparison using a key function.
"""

from typing import TypeVar, Callable

T = TypeVar('T')

def compare(x: T, y: T, key: Callable[[T], any] = None) -> int:
    """
    Compare two objects of the same type.

    Args:
        x (T): The first object to compare.
        y (T): The second object to compare.
        key (Callable[[T], any], optional): A function to extract a key from each object for comparison.
            Defaults to None, which means direct comparison of objects.

    Returns:
        int: -1 if x < y, 0 if x == y, 1 if x > y.
    """
    if key is not None:
        #todo
        x_key = key(x)
        y_key = key(y)
        if x_key < y_key:
            return -1
        elif x_key == y_key:
            return 0
        else:
            return 1
    else:
        #todo
        if x < y:
            return -1
        elif x == y:
            return 0
        else:
            return 1

# Example usage:

# Direct comparison
print(compare(5, 10))  # Output: -1
print(compare("abc", "abc"))  # Output: 0
print(compare(20, 10))  # Output: 1


# Comparison with key function
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort students by age
sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)  # Output: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
