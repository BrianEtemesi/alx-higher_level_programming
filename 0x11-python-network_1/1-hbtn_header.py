#!/usr/bin/python3
"""
script to display value of a variable found in the header of the response
"""

import urllib.request
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        pass
    print(response.getheader("X-Request-Id"))
