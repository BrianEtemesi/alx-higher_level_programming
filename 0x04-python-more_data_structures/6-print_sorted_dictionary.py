#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_d = dict(sorted(a_dictionary.items()))
    for key, value in sorted_d.items():
        print("{}: {}".format(key, value))
