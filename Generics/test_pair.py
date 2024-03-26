
import unittest
from pair import Pair

class TestPair(unittest.TestCase):
    def test_pair_creation(self):
        # Create a pair of integers and strings
        pair1 = Pair(1, "apple")
        self.assertEqual(pair1.first, 1)
        self.assertEqual(pair1.second, "apple")

        # Create a pair of float and list
        pair2 = Pair(3.14, [1, 2, 3])
        self.assertEqual(pair2.first, 3.14)
        self.assertEqual(pair2.second, [1, 2, 3])

        # Create a pair of tuple and dictionary
        pair3 = Pair((1, 2), {"a": 1, "b": 2})
        self.assertEqual(pair3.first, (1, 2))
        self.assertEqual(pair3.second, {"a": 1, "b": 2})

    def test_pair_representation(self):
        # Create a pair of integers and strings
        pair1 = Pair(1, "apple")
        self.assertEqual(repr(pair1), "Pair(1, apple)")

        # Create a pair of float and list
        pair2 = Pair(3.14, [1, 2, 3])
        self.assertEqual(repr(pair2), "Pair(3.14, [1, 2, 3])")

        # Create a pair of tuple and dictionary
        pair3 = Pair((1, 2), {"a": 1, "b": 2})
        self.assertEqual(repr(pair3), "Pair((1, 2), {'a': 1, 'b': 2})")

if __name__ == "__main__":
    unittest.main()