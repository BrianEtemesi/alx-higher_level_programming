#!/bin/bash
# This script takes in a URL as and argument, sends a request
# to the URL and displays the size of the body of the response

curl -s "$1" -w '%{size_download}\n' -o /dev/null
