#!/usr/bin/python3

def max_integer(my_list=[]):
    max_ = my_list[0]
    for i in range(len(my_list) - 1):
        if my_list[i] > max_:
            max_ = my_list[i]
    return max_
