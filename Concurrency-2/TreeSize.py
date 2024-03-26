import threading
from concurrent.futures import Executor, as_completed

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class TreeSizeCalculator:
    def __init__(self, root: Node, executor: Executor):
        self.root = root
        self.executor = executor
        self.size = 0

    def calculate_size(self):
        if self.root:
            self._calculate_size_recursive(self.root)

    def _calculate_size_recursive(self, node: Node):
        if node:
            self.size += 1
            futures = []
            if node.left:
                futures.append(self.executor.submit(self._calculate_size_recursive, node.left))
            if node.right:
                futures.append(self.executor.submit(self._calculate_size_recursive, node.right))
            for future in as_completed(futures):
                future.result()


# Unit Testing
import unittest

class TestTreeSizeCalculator(unittest.TestCase):
    def test_tree_size(self):
        # Creating a binary tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        # Now, the as_completed function is used to iterate over the futures returned by the executor,
        # ensuring that we wait for all threads to finish before asserting the size of the binary tree.
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            tree_calculator = TreeSizeCalculator(root, executor)
            tree_calculator.calculate_size()

        self.assertEqual(tree_calculator.size, 7)

if __name__ == '__main__':
    unittest.main()