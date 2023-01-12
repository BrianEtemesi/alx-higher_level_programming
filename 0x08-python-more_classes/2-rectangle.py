#!/usr/bin/python3

"""Execution of a rectangle class representing a rectangle with
private attributes: width and height, and public method for finding
the area and perimeter of the rectangle
"""


class Rectangle:
    """class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes rectangle with width and height values"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """retreives/returns the width attribute of a rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """update the width value of a rectangle instance"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retreives/returns the height attribute of a rectangle instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """updates the height attribute of a rectangle instance"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """derives the area of a rectangle instance"""

        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
