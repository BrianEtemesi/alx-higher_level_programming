#!/usr/bin/python3
"""
class that defines a Square with a private size attribute,
setter and getter to access and update attribute
"""


class Square:
    """class to represent a square"""

    def __init__(self, size=0):
        """initializes square with size"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """derives area of a square instance"""

        return self.__size ** 2

    def my_print(self):
        """prints square to stdout using '#' """

        if self.__size == 0:
            print("")
        else:
            x = 0
            y = self.__size
            while x < self.__size:
                for i in range(y):
                    if i == (y - 1):
                        print("#")
                    else:
                        print("#", end="")
                x += 1

    @property
    def size(self):
        """retrives/returns the size of a square instance"""

        return self.__size

    @size.setter
    def size(self, size):
        """updates the size attribute of a square instance"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
