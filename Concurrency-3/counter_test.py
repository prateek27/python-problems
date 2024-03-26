import threading
import unittest
import time
from counter import Counter


class TestCounter(unittest.TestCase):
    def test_concurrent_counter(self):
        # Initialize counter with initial value 0
        counter = Counter(0)

        # Function for concurrent increment operation
        def concurrent_inc(offset):
            for _ in range(100000):
                counter.incValue(offset)

        # Function for concurrent decrement operation
        def concurrent_dec(offset):
            for _ in range(50000):
                counter.decValue(offset)

        # Create and start multiple threads for concurrent increment and decrement
        threads = []
        for _ in range(10):
            thread_inc = threading.Thread(target=concurrent_inc, args=(1,))
            thread_dec = threading.Thread(target=concurrent_dec, args=(1,))
            threads.append(thread_inc)
            threads.append(thread_dec)
            thread_inc.start()
            thread_dec.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Check if counter value is 0 after concurrent operations
        self.assertEqual(counter.getValue(), 500000)


if __name__ == "__main__":
    unittest.main()