#!/bin/bash
# send GET request to URL and only display body of a `200` status code response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
