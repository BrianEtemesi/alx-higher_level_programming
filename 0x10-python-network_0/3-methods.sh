#!/bin/bash
# displays all HTTP methods a server will accept
curl -s -I -X OPTIONS "$1"
