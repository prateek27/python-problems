"""Given a list of strings representing sentences, write a python method called processSentences that performs the following operations using Java streams:
Filter out sentences that contain the word "python".
Map each remaining sentence to its length.
Find the average length of the sentences.
Convert the average length to an integer by rounding down.
Return the rounded average length."""

def processSentences(sentences):
    """
    Perform operations on sentences:
    1. Filter out sentences containing the word "python".
    2. Map each remaining sentence to its length.
    3. Find the average length of the sentences.
    4. Convert the average length to an integer by rounding down.

    Args:
    - sentences: A list of strings representing sentences

    Returns:
    - The rounded average length of the remaining sentences
    """
    # Filter out sentences containing the word "python"
    filtered_sentences = [sentence for sentence in sentences if "python" in sentence.lower()]

    # Map each remaining sentence to its length
    sentence_lengths = [len(sentence) for sentence in filtered_sentences]

    # Find the average length of the sentences
    if sentence_lengths:
        average_length = sum(sentence_lengths) / len(sentence_lengths)
    else:
        average_length = 0

    # Convert the average length to an integer by rounding down
    rounded_average_length = int(average_length)

    return rounded_average_length


