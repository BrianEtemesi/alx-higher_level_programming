#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json


class Base:
    """Base class of other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new instances with an id"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON string representation of list dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            jstr = json.dumps(list_dictionaries)
            return jstr
