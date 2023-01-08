#!/usr/bin/python3
"""
write a class that defines a square
validate the size to be an integer not less than zero.
"""


class Square:
    """represents a square with an optinal size attribute."""

    def __init__(self, size=0):
        """Initializes size of square."""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
