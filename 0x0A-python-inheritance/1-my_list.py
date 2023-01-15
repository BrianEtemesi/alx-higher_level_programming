#!/usr/bin/python3
"""
Execution a class representing a list ``MyList`` that inherits
from the built-in python list.
"""


class MyList(list):
    """ class representing a list ``MyList`` """

    def print_sorted(self):
        """sorts list in ascending order and prints"""

        a = list(self)
        a.sort()
        print(a)
