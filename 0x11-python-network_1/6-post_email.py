#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a post request
to the URL with email as the parameter, then displays the response
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    email = {'email': argv[2]}

    res = requests.post(url, data=email)
    print(res.text)
