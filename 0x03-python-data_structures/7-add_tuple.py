#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        x = tuple_a[0]
        y = tuple_a[1]
    elif len(tuple_a) == 1:
        x = tuple_a[0]
        y = 0
    else:
        x = 0
        y = 0

    if len(tuple_b) >= 2:
        x1 = tuple_b[0]
        y1 = tuple_b[1]
    elif len(tuple_b) == 1:
        x1 = tuple_b[0]
        y1 = 0
    else:
        x1 = 0
        y1 = 0

    tuple_3 = (x + x1), (y + y1)
    return tuple_3
