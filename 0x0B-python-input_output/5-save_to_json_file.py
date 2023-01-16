#!/usr/bin/python3
"""
Implementation of a function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON
    representation.

    Aargs:
        my_obj: Object

        filename: Text file

    """

    string_rep = json.dumps(my_obj)

    with open(filename, mode='w', encoding='utf=8') as a_file:
        a_file.write(string_rep)
