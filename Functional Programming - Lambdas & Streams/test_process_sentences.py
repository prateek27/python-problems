import unittest
from process_sentences import processSentences

class TestProcessSentencesTestCase(unittest.TestCase):
    def test_process_sentences(self):
        sentences = ["python is a programming language", "I love java", "python is versatile"]
        # Filtered sentences: ["I love Java"]
        # Lengths: [11]
        # Average length: 11
        # Rounded average length: 11
        self.assertEqual(processSentences(sentences), 25)

    def test_empty_list(self):
        sentences = []
        # No sentences to process, so expected result is 0
        self.assertEqual(processSentences(sentences), 0)

    def test_no_python_sentences(self):
        sentences = ["Java is my favorite language", "I am learning JavaScript"]
        # No sentences contain "python", so expected result is 0
        self.assertEqual(processSentences(sentences), 0)


if __name__ == "__main__":
    unittest.main()