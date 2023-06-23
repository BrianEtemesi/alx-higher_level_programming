#!/usr/bin/python3
"""
defines a class that inherits from `int`
"""


class MyInt(int):
    """
    Class that inherits from class int
    """

    def __eq__(self, other):
        """
        Returns != check
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        Returns == check
        """
        return int.__eq__(self, other)
