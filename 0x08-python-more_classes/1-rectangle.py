#!/usr/bin/python3
"""Execution of a Rectangle class representing a
a rectangle with private instance attribures; width and height.
"""


class Rectangle:
    """class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes rectangle instance with width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves/returns width of rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """updates width attribute of a rectangle instance"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieves/returns the height of a rectangle instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """updates height attribute of rectangle instance"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
