"""Write a Python function called word_frequencies that takes a list of strings as input and returns a dictionary containing the frequency of each word in the input list.

Your function should perform the following steps using functional programming concepts:

Flatten the list: Convert the list of strings into a single string.
Tokenization: Split the string into individual words.
Normalization: Convert all words to lowercase to treat uppercase and lowercase versions of the same word as equal.
Word Counting: Count the frequency of each word.
Result: Return a dictionary containing each word and its frequency.
"""

from typing import List, Dict
import re
from collections import Counter


def word_frequencies(sentences: List[str]) -> Dict[str, int]:

    # todo:Flatten the list and join all sentences into a single string
    text = ' '.join(sentences)

    # todo: Tokenization: Split the string into individual words
    words = re.findall(r'\b\w+\b', text.lower())

    # todo: Word Counting: Count the frequency of each word
    word_counts = Counter(words)

    # todo
    return dict(word_counts)


sentences = [
    "Python is a popular programming language",
    "I love coding in Python",
    "Java is also a great language"
]

# Get word frequencies
result = word_frequencies(sentences)

# Print the result
print(result)

# Expected Output:
# {'python': 2, 'is': 2, 'a': 2, 'popular': 1, 'programming': 1, 'language': 2, 'i': 1, 'love': 1, 'coding': 1, 'in': 1, 'java': 1, 'also': 1, 'great': 1}


