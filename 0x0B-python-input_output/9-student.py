#!/usr/bin/python3
"""
defines a Student class
"""


class Student:
    """
    Class representation of a student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes an instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns directory description
        """
        return self.__dict__.copy()
