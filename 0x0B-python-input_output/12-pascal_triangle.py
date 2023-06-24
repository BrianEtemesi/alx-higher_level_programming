#!/usr/bin/python3
"""
function to return list of integers representing
pascals triangle
"""


def pascal_triangle(n):
    """
    returns the pascal triangle
    """

    my_list = []
    prev = []

    for i in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p1] + prev[p2]]
            p1 += 1
            p2 += 1
        my_list.append(res_list)
        prev = res_list[:]

    return my_list
