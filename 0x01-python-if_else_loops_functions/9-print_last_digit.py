#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    c = number % 10
    print("{}".format(c), end='')
    return c
