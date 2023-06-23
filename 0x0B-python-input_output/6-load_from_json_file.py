#!/usr/bin/python3
"""
function that create object from json file
"""
import json


def load_from_json_file(filename):
    """
    returns an object by a JSON representation
    """
    with open(filename, 'r') as file:
        return json.load(file)
