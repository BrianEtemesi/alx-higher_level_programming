#!/usr/bin/python3
"""
Defines a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """
    Returns an object by a JSON representation
    """
    with open(my_str, 'r') as file:
        return json.load(file)
