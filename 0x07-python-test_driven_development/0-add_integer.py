#!/usr/bin/python3

"""

Execution of a function that adds 2 integers

"""


def add_integer(a, b=98):
    """adds two integers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the 2 numbers

    Raises:
        TypeError if either a or b is not a float or an integer
    """

    if type(a) != int and type(a) != float:
        """check if `a` is a float or integer"""

        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
