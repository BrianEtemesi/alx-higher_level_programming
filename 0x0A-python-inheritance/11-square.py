#!/usr/bin/python3
"""
square with str method
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a Square from Rectangle class
    """

    def __init__(self, size):
        """
        initializes a Square instance
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        returns area
        """
        return super().area()

    def __str__(self):
        """
        return string represantation of a square instance 
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
