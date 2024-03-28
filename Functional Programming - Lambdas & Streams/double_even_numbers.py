def is_even(num):
    """
    Check if a number is even.

    Args:
    - num: An integer

    Returns:
    - True if the number is even, False otherwise
    """
    return num % 2 == 0


def double(num):
    """
    Double a number.

    Args:
    - num: An integer

    Returns:
    - The doubled value of the input number
    """
    return num * 2


def filter_and_double_even_numbers(numbers):
    """
    Filter even numbers from the input list and double them.

    Args:
    - numbers: A list of integers

    Returns:
    - A list containing doubled values of even numbers from the input list
    """

    #todo
    return list(map(double, filter(is_even, numbers)))