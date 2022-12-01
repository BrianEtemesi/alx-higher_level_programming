#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv)
    if (l < 2):
        print("{} arguments.".format(l - 1))
    elif (l == 2):
        print("{} argument:\n{}: {}".format(1, 1, sys.argv[1]))
    else:
        print("{} arguments:".format(l - 1))
        i = 1
        while (i < l):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
