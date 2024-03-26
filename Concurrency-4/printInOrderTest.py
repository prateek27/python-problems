# Unit tests
import unittest
import threading
from printInOrder import Foo

class TestFoo(unittest.TestCase):
    def test_sequence(self):
        foo = Foo()

        # Create threads for calling first(), second(), and third()
        thread_first = threading.Thread(target=foo.first)
        thread_second = threading.Thread(target=foo.second)
        thread_third = threading.Thread(target=foo.third)

        # Start threads in reverse order (third(), second(), first())
        thread_third.start()
        thread_second.start()
        thread_first.start()

        # Wait for all threads to complete
        thread_first.join()
        thread_second.join()
        thread_third.join()

        # Verify the output sequence
        self.assertSequenceEqual(["first", "second", "third"], foo.output)

if __name__ == "__main__":
    unittest.main()