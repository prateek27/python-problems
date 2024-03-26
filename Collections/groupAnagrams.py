from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    # Group anagrams using a dictionary
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)

    # Convert the values of the dictionary to lists and return
    return list(anagrams.values())


# Example usage
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strings))
