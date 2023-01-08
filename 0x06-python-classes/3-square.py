#!/usr/bin/python3
"""
class Square with private instance attribute size that
returns area using a public instance method
"""


class Square:
    """Represents a square with attributes size and area"""

    def __init__(self, size=0):
        """Initializes square with size."""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """derives the area of the square using size"""

        return self.__size ** 2
