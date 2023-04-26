#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to URL
http://0.0.0.0:5000/search_user with the letter as parameter
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    try:
        values = {'q': argv[1]}
    except IndexError:
        values = {'q': ""}
    res = requests.post(url, data=values)
    try:
        to_json = res.json()
    except TypeError:
        print("Not a valid JSON")

    name = to_json.get('name')
    user_id = to_json.get('id')

    if (name is None or user_id is None):
        print("No result")
    else:
        print("[{}] {}".format(user_id, name))
