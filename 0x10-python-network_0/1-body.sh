#!/bin/bash
# sends a GET request to the URL
# Check if a URL argument is provided

target_url="$1"

# Check if the HTTP status code from the HEAD request is 200
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$target_url") == '200' ]; then
    # If the status code is 200, fetch and display the response body
    curl -Ls "$target_url"
fi
