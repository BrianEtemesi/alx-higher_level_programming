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

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves/returns the height attribute of a rectangle instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """updates the height attribute of a rectangle instance"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the x cordinate attribute of a rectangle instance"""

        return self.__x

    @x.setter
    def x(self, value):
        """updates the x cordinate attribute of a rectangle instance"""

        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """returns the y cordinate attribute of a rectangle instance"""

        return self.__y

    @y.setter
    def y(self, value):
        """updates the y cordinate attribute of a rectangle instance"""

        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """derives the area of a rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """prints rectangle to stdout using '#' """

        for i in range(self.__y):
            print()

        for i in range(self.__height):
            k = 1
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                if k == self.__width:
                    print("#")
                else:
                    print("#", end='')
                k += 1

    def __str__(self):
        """returns specified details of a rectangle instance"""

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
