import threading
import math

#Todo: implement the factorial thread class
class FactorialThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = None

    def run(self):
        self.result = math.factorial(self.n)

def compute_large_factorial(n):
    # Todo: Create a factorial thread
    thread = FactorialThread(n)
    # Todo
    thread.start()
    # Todo: wait for calc to finish by calling the join method
    thread.join()

    #Todo: return the result
    return thread.result

# Unit tests
import unittest

class TestFactorialThread(unittest.TestCase):
    def test_thread_used(self):
        n = 1000
        result = compute_large_factorial(n)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, int))
        self.assertTrue(result > 0)

    def test_result(self):
        n = 5
        result = compute_large_factorial(n)
        self.assertEqual(result, math.factorial(n))

if __name__ == '__main__':
    unittest.main()