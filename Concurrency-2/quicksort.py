import concurrent.futures
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_left = executor.submit(quicksort, left)
        future_right = executor.submit(quicksort, right)
    return future_left.result() + middle + future_right.result()

# Example usage:
arr = random.sample(range(1, 100), 20)
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)

