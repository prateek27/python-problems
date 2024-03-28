import unittest
from unittest.mock import patch
import io
from valid_book_name import *

class TestBookNameValidator(unittest.TestCase):
    def test_valid_book_name(self):
        book_name = "Introduction to Scaler Java"
        with self.assertRaises(InvalidBookNameException) as context:
            BookNameValidator.validate(book_name)
        self.assertEqual(str(context.exception), "Book name doesn't start with Scaler Java")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_book_name(self, mock_stdout):
        book_name = "Scaler Java: Introduction to Algorithms"
        expected_output = "Book created!: " + book_name
        BookNameValidator.validate(book_name)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()