#!/usr/bin/python3
def safe_print_integer(value):
    """Safely print an integer value using the "{:d}".format() method.

    Args:
        value (int): The integer to be printed.

    Returns:
        If no exception occurs - True.
        Otherwise - False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
