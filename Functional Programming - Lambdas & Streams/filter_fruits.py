"""Use functional programming concepts to write a function to filter out fruits from a list which start with A or a"""

def filter_fruits_starting_with_a(fruits):
    """
    Filter fruits starting with 'A' or 'a'.

    Args:
    - fruits: A list of fruit strings

    Returns:
    - A list containing only fruits starting with 'A' or 'a'
    """
    return list(filter(lambda fruit: fruit.startswith('a') or fruit.startswith('A'), fruits))

