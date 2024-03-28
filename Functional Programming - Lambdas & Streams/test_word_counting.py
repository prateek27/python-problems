# Unit tests
import unittest
from word_counting import word_frequencies

class TestWordFrequencies(unittest.TestCase):
    def test_word_frequencies(self):
        sentences = [
            "Python is a popular programming language",
            "I love coding in Python",
            "Java is also a great language"
        ]
        expected_result = {
            'python': 2,
            'is': 2,
            'a': 2,
            'popular': 1,
            'programming': 1,
            'language': 2,
            'i': 1,
            'love': 1,
            'coding': 1,
            'in': 1,
            'java': 1,
            'also': 1,
            'great': 1
        }
        self.assertEqual(word_frequencies(sentences), expected_result)

    def test_empty_input(self):
        sentences = []
        self.assertEqual(word_frequencies(sentences), {})

    def test_case_insensitivity(self):
        sentences = [
            "Python is Awesome",
            "python is great",
            "PYTHON is fantastic"
        ]
        expected_result = {
            'python': 3,
            'is': 3,
            'awesome': 1,
            'great': 1,
            'fantastic': 1
        }
        self.assertEqual(word_frequencies(sentences), expected_result)

    def test_punctuation_handling(self):
        sentences = [
            "Python is, awesome!",
            "Python is great",
            "Python, Python, Python!!!"
        ]
        expected_result = {
            'python': 5,
            'is': 2,
            'awesome': 1,
            'great': 1
        }
        self.assertEqual(word_frequencies(sentences), expected_result)

if __name__ == "__main__":
    unittest.main()