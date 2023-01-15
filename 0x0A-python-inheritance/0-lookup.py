#!/usr/bin/python3
"""Execution of a function that returns all the attributes and
methods of an object
"""

def lookup(obj):
    """returns a list of available attributes of a class"""

    return dir(obj)
