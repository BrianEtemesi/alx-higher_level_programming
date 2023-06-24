#!/usr/bin/python3
"""
defines a class to return the dictionary description for
jJSON serialization of an object
"""


def class_to_json(obj):
    """
    retuns dictionary description of an obj
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
