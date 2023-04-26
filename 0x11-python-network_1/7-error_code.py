#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    res = requests.get(url)

    err_code = res.status_code
    if err_code >= 400:
        print("Error code: {}".format(err_code))
    else:
        print(res.text)
