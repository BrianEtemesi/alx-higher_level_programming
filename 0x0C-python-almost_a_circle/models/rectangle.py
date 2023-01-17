#!/usr/bin/python3
"""Implementation of a rectangle class that inherits
from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class representation of a rectangle
    The Rectangle class inherits from a superclass(Base)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance with dimension
        and cordinate attributes
        """

        Base.__init__(self, id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves/returns the width attribute of a rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """updates the width attribute of a rectangle instance"""

        self.__width = value

    @property
    def x(self):
        """returns the x cordinate attribute of a rectangle instance"""

        return self.__x

    @x.setter
    def x(self, value):
        """updates the x cordinate attribute of a rectangle instance"""

        self.__x = value

    @property
    def y(self):
        """returns the y cordinate attribute of a rectangle instance"""

        return self.__y

    @y.setter
    def y(self, value):
        """updates the y cordinate attribute of a rectangle instance"""

        self.__y = value
