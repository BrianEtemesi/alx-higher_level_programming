#!/usr/bin/python3
"""
write a class representing a square with private
attributes; size and position. public methods; area and
my_print.
"""


def posError():
    """raises TypeError is position conditions are not met"""

    raise TypeError("position must be a tuple of 2 positive integers")


class Square:
    """class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes square with size and position"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple:
            posError()
        if len(position) != 2:
            posError()
        if type(position[0]) != int or type(position[1]) != int:
            posError()
        if position[0] < 0 or position[1] < 0:
            posError()
        self.__position = position

    def area(self):
        """derives area of square using the size attribute"""

        return self.__size ** 2

    def my_print(self):
        """prints square to stdout using '#'"""

        if self.__size == 0:
            print()
        else:
            x = 0
            y = self.__size
            for i in range(self.__position[1]):
                print()
            while x < self.__size:
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(y):
                    if i == (y - 1):
                        print("#")
                    else:
                        print("#", end="")
                x += 1

    @property
    def size(self):
        """retrieves/returns size of square instance"""

        return self.__size

    @size.setter
    def size(self, size):
        """updates size attribute of square"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """retrieves position of square instance"""

        return self.__position

    @position.setter
    def position(self, value):
        """updates position of square instance"""

        if type(value) != tuple:
            posError()
        if len(value) != 2:
            posError()
        if type(value[0]) != int or type(value[1]) != int:
            posError()
        if value[0] < 0 or value[1] < 0:
            posError()
        self.__position = value
