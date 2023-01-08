#!/usr/bin/python3
"""
Write a square class with methods to
access and update private attributes.
"""


class Square:
    """Represents a square with size, area attributes"""

    def __init__(self, size=0):
        """Initializes size of square instance"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of a square"""

        return self.__size ** 2

    @property
    def size(self):
        """retrieves/returns size of a square instance"""

        return self.__size

    @size.setter
    def size(self, size):
        """updates/sets size attribute of a square instance"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
