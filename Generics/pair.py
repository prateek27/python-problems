"""We define a generic Pair class that takes two type parameters T and U representing the types of the first and second elements of the pair, respectively.
The constructor __init__ initializes the pair with the given first and second elements.
We provide a __repr__ method to customize the string representation of the pair.
We demonstrate the usage of the Pair class with examples of creating pairs of various types.
"""

from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Pair:
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"

# Example usage:

# Create a pair of integers and strings
pair1 = Pair(1, "apple")
print(pair1)  # Output: Pair(1, apple)

# Create a pair of float and list
pair2 = Pair(3.14, [1, 2, 3])
print(pair2)  # Output: Pair(3.14, [1, 2, 3])

# Create a pair of tuple and dictionary
pair3 = Pair((1, 2), {"a": 1, "b": 2})
print(pair3)  # Output: Pair((1, 2), {'a': 1, 'b': 2})



