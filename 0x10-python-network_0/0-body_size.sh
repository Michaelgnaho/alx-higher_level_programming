#!/usr/bin/python3
# This script to get the body size of a request
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '