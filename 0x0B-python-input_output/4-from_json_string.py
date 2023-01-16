#!/usr/bin/python3
"""
Implementation of a function that returns an
object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Takes a string represantation of a JSON object, deserializes it
    and returns a python object.
    """

    return json.loads(my_str)
