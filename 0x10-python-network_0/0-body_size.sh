#!/bin/bash
# curl URL passesd as argument and display the size of body of response
curl -s "$1" -w '%{size_download}\n' -o /dev/null
