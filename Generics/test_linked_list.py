import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append(self):
        # Create a linked list of integers
        ll_int = LinkedList[int]()
        ll_int.append(1)
        ll_int.append(2)
        ll_int.append(3)

        # Verify the linked list contains the correct elements
        self.assertEqual(ll_int.head.data, 1)
        self.assertEqual(ll_int.tail.data, 3)

        # Verify the linked list is correctly linked
        self.assertEqual(ll_int.head.next.data, 2)
        self.assertEqual(ll_int.tail.next, None)

    def test_print_list(self):
        # Create a linked list of strings
        ll_str = LinkedList[str]()
        ll_str.append("a")
        ll_str.append("b")
        ll_str.append("c")

        # Redirect stdout to a StringIO object to capture print output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        ll_str.print_list()
        output = sys.stdout.getvalue()

        # Reset stdout
        sys.stdout = original_stdout

        # Verify the printed output matches the expected output
        expected_output = "a -> b -> c -> None\n"
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()