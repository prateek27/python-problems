from typing import TypeVar, List

# find max - restrict the input types to int or float
"""We use a type variable T with bounds int and float
The find_max function takes a list of elements of type T.
We initialize max_value with the first element of the list and iterate over the remaining elements, updating max_value if we encounter a larger element.
Finally, we return the maximum value found."""

#todo
T = TypeVar('T', int, float)


def find_max(arr: List[T]) -> T:
    if not arr:
        raise ValueError("List is empty")

    #todo
    max_value = arr[0]
    for item in arr:
        if item > max_value:
            max_value = item
    return max_value


# Example usage:
int_list = [1, 5, 3, 7, 2]
float_list = [2.5, 4.7, 3.2, 6.1, 5.0]

print(find_max(int_list))  # Output: 7
print(find_max(float_list))  # Output: 6.1

