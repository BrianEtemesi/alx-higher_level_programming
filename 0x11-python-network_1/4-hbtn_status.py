#!/usr/bin/python3
"""
this is a script to fetch from url: https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.encoding)))
    print("\t- content: {}".format(res.text))
