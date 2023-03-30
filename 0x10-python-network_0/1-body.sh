#!/bin/bash
# send GET request to URL and only display body of a `200` status code response
curl -s -f -L "$1"
