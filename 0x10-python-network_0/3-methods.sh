#!/bin/bash
# displays all HTTP methods a server will accept
curl -s -I -X OPTIONS "$1" | grep -i Allow | cut -d ' ' -f2-
