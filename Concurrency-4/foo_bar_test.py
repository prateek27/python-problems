import unittest
from foo_bar import FooBar
import threading
from io import StringIO
import sys

class TestFooBar(unittest.TestCase):
    def test_foobar(self):
        n = 5
        fb = FooBar(n)

        # Redirect stdout to a StringIO object
        output = sys.stdout = StringIO()

        def foo():
            fb.foo()

        def bar():
            fb.bar()

        threads = []
        threads.append(threading.Thread(target=foo))
        threads.append(threading.Thread(target=bar))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        # Reset sys.stdout to the original stdout
        sys.stdout = sys.__stdout__

        # Check the output
        output_str = output.getvalue()
        self.assertEqual(len(output_str), 6 * n)  # Each "foobar" has length 6
        self.assertEqual(output_str, 'foobar' * n)

if __name__ == "__main__":
    unittest.main()
