#!/usr/bin/python3
"""
defines a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """
    Returns an object by a JSON representation
    """
    return json.loads(my_str)
