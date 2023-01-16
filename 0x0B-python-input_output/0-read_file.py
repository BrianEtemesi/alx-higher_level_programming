#!/usr/bin/python3
"""
Implementation of a function that reads a text file
and prints it to stdout
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""

    with open(filename, encoding='utf-8') as a_file:
        x = a_file.read()
        print(x, end="")
