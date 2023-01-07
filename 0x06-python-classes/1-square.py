#!/usr/bin/python3

"""write a class that defines a square
and initialize size as a private attribute
"""


class Square:
    """defines a class called Square"""

    def __init__(self, size):
        """initialize size of square"""
        self.__size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
