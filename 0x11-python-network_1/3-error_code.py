#!/usr/bin/python3
"""
This script sends a request to the url passed and displays
body of the response, manages HTTP error exceptions
"""
import urllib
from urllib import request
from sys import argv

if __name__ == "__main__":

    req = request.Request(argv[1])
    try:
        body = request.urlopen(req)
        print(body.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
