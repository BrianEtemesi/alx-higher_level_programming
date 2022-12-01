#!/usr/bin/python3
import sys

if __name__ == "__main__":
    res = 0
    n = len(sys.argv)
    i = 1
    while (i < n):
        res += int(sys.argv[i])
        i += 1
    print("{}".format(res))
