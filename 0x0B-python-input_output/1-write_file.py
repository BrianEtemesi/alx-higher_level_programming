#!/usr/bin/python3
"""
Implementaion of a function that writes a string to a
text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns
    the number of characters written

    Args:
        filename: text file

        text: string

    """

    with open(filename, mode='w', encoding='utf=8') as a_file:
        return a_file.write(text)
