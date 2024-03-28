"""I defined a custom exception class DivisionByZeroError that inherits from the base Exception class. This custom exception is raised when attempting to divide by zero.
The divide_numbers() function now checks if the divisor is zero and raises a DivisionByZeroError with a custom error message if so."""

class DivisionByZeroError(Exception):
    """Custom exception raised when attempting to divide by zero."""
    # don't modify this custom exception class
    pass


def divide_numbers(dividend, divisor):
    """
    Divide two numbers.

    Args:
    - dividend: The number to be divided (numerator)
    - divisor: The number to divide by (denominator)

    Returns:
    - The result of the division
    """

    # todo : raise DivisionByZeroError if divisor is zero, return result otherwise
    if divisor == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return dividend / divisor


