#!/usr/bin/python3
"""Implementation of a 'Square' class that inherits
from a superclass 'Rectangle' """
from models.rectangle import Rectangle


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
