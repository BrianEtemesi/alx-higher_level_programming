#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copy = {}
    values = list(a_dictionary)
    for i in values:
        copy[i] = a_dictionary[i] * 2
    return copy
