import unittest
from io import StringIO
import sys
import time
from Threads import Adder, Subtractor, Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.adder_output = StringIO()
        self.subtractor_output = StringIO()
        sys.stdout = self.adder_output  # Redirect stdout to capture printed output
        adder_thread = Adder()
        adder_thread.start()
        adder_thread.join()
        self.adder_output_value = self.adder_output.getvalue().strip()

        self.subtractor_output = StringIO()
        sys.stdout = self.subtractor_output  # Redirect stdout to capture printed output
        subtractor_thread = Subtractor()
        subtractor_thread.start()
        subtractor_thread.join()
        self.subtractor_output_value = self.subtractor_output.getvalue().strip()

    def tearDown(self):
        sys.stdout = sys.__stdout__  # Reset redirect

    def test_adder_output(self):
        self.assertEqual(self.adder_output_value, "I am the Adder class")

    def test_subtractor_output(self):
        self.assertEqual(self.subtractor_output_value, "I am the Subtractor class")

    def test_main_output(self):
        main_output = StringIO()
        sys.stdout = main_output
        Client.main()
        main_output_value = main_output.getvalue().strip()
        self.assertEqual(main_output_value, "I am the main class\nI am the Adder class\nI am the Subtractor class")

if __name__ == '__main__':
    unittest.main()