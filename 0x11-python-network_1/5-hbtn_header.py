#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    res = requests.get(url)
    h_value = res.headers['X-Request-Id']
    print(h_value)
