#!/usr/bin/python3

"""Execution of a function that adds 2 integers
foo
bar
foo
"""


def add_integer(a, b=98):
    """adds two integers
    check
    """

    if type(a) != int and type(a) != float:
        """check if `a` is a float or integer"""

        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
