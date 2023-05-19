#!/usr/bin/env bash
# Script to transfer files to a remote server

# check if all arguments are provided
if [ $# -ne 3 ];
then
	echo "Usage: $0 <file> <username> <hostname>"
	exit 1
fi

file="$1"
username="$2"
hostname="$3"

# transfer file using scp
scp "$file" "$username@$hostname:~/" # add ~/ to save file in home directory of remote server
