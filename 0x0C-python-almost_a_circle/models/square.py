#!/usr/bin/python3
"""Implementation of a 'Square' class that inherits
from a superclass 'Rectangle' """
from models.rectangle import Rectangle
import inspect


class Square(Rectangle):
    """Class representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes attributes to a square instance"""

        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """returns specified details of a square instance"""

        s_square = "[{}] ".format(type(self).__name__)
        s_id = "({}) ".format(self.id)
        s_x_y = "{}/{} ".format(self.x, self.y)
        s_size = "- {}".format(self.width)

        return s_square + s_id + s_x_y + s_size

    @property
    def size(self):
        """returns/retrieves the size of a square instance"""

        return self.width

    @size.setter
    def size(self, value):
        """updates the value of size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes with arguments passed"""

        attr_list = ["id", "size", "x", "y"]
        if len(args) > 0:
            if len(args) > 4:
                raise IndexError("Arguments should be <= 4")
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of a square object"""

        sq = {}
        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith('_') and not inspect.ismethod(value):
                if name != 'height' and name != 'width':
                    sq[name] = value
        return sq
