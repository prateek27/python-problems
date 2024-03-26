# Unit tests
import unittest
from unittest.mock import patch
from io import StringIO
from Adder import Adder,Client

class TestClient(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '7'])
    def test_main(self, mock_input):
        expected_output = "12\n"
        with StringIO() as mock_output:
            with patch('sys.stdout', mock_output):
                Client.main()
                self.assertEqual(mock_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()