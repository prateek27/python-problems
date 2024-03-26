import unittest
import threading
from zero_even_odd import ZeroEvenOdd, PrintNumber
from io import StringIO
import sys

class TestZeroEvenOdd(unittest.TestCase):
    def test_zero_even_odd(self):
        n = 5
        zeo = ZeroEvenOdd(n)
        pn = PrintNumber()

        # Redirect stdout to a StringIO object
        output = sys.stdout = StringIO()

        def zero():
            zeo.zero(pn)

        def even():
            zeo.even(pn)

        def odd():
            zeo.odd(pn)

        threads = []
        threads.append(threading.Thread(target=zero))
        threads.append(threading.Thread(target=even))
        threads.append(threading.Thread(target=odd))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        # Reset sys.stdout to the original stdout
        sys.stdout = sys.__stdout__

        # Check the output
        output_str = output.getvalue()
        expected_output = "0102030405";
        self.assertEqual(output_str, expected_output)

if __name__ == "__main__":
    unittest.main()