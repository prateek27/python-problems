# Unit tests
import unittest
from io import StringIO
from TableCreator import TableCreator

class TestTableCreator(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.table_creator = TableCreator(3)
        self.table_creator.output = self.output

    def test_table_creation(self):
        expected_output = "3 times 1 is 3\n3 times 2 is 6\n3 times 3 is 9\n3 times 4 is 12\n3 times 5 is 15\n3 times 6 is 18\n3 times 7 is 21\n3 times 8 is 24\n3 times 9 is 27\n3 times 10 is 30\n"
        self.table_creator.run()
        self.assertEqual(self.output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()