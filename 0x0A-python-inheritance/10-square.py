#!/usr/bin/python3
"""
defines a square that inherites from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle superclass
    """
    def __init__(self, size):
        """
        Method that initializes a Square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Method that returns a string with the area
        """

        return super().area()
