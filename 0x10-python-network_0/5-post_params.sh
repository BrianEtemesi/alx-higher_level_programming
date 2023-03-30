#!/bin/bash
# sends POST request and key-value pair parameters to a URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
