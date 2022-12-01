#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    if (n < 2):
        print("{} arguments.".format(n - 1))
    elif (n == 2):
        print("{} argument:\n{}: {}".format(1, 1, sys.argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        i = 1
        while (i < n):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
