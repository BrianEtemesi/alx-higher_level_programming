#!/usr/bin/python3
"""
Execution of a function that appends a string at the end
of a text file and returns the number of characters added
If the file doesnt exist, it should be created
"""


def append_write(filename="", text=""):
    """appends a string at the end of a textfile then
    returns the number of characters added
    """

    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
