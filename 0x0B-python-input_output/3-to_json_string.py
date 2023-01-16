#!/usr/bin/python3
import json

"""
Implementaion of a function that returns the JSON
representation of an object.
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""

    return json.dumps(my_obj)
