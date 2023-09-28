#!/bin/bash
# sends a GET request to the URL
# Check if a URL argument is provided
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then
    URL="$1"
    curl -Ls "$URL"
fi
