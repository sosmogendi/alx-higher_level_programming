#!/bin/bash
# script to get the allowed methods in a server if available through OPTIONS http request
curl -s -I -X OPTIONS "$1" | awk '/^Allow:/ {print substr($0, 8)}'
