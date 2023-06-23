#!/usr/bin/python3
"""
defines a class to check inherited class
"""


def inherits_from(obj, a_class):
    """
    Returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type
    """
    
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
