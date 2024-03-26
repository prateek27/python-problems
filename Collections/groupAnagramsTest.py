import unittest
from groupAnagrams import group_anagrams

class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_empty_input(self):
        input_strings = []
        expected_output = []
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_single_string(self):
        input_strings = ["hello"]
        expected_output = [["hello"]]
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_no_anagrams(self):
        input_strings = ["abc", "def", "ghi"]
        expected_output = [["abc"], ["def"], ["ghi"]]
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_mixed_anagrams(self):
        input_strings = ["abcd", "dcba", "efgh", "hgef", "ijk", "kji"]
        expected_output = [["abcd", "dcba"], ["efgh", "hgef"], ["ijk", "kji"]]
        self.assertEqual(group_anagrams(input_strings), expected_output)

if __name__ == "__main__":
    unittest.main()