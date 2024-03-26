def count_frequency(arr):
    #todo
    frequency = {}
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

# Example usage:
arr = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
frequency = count_frequency(arr)
print(frequency)