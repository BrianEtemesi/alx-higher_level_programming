#!/usr/bin/python3
"""
define a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends a new line when a string is found
    """

    output = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            output += [line]
            if line.find(search_string) != -1:
                output += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(output))
