#!/bin/bash
# Send a GET request to a URL and display the response body for a 200 status code

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract the URL from the command-line argument
url="$1"

# Send a HEAD request to get the response code
response_code=$(curl -L -s -X HEAD -w "%{http_code}" "$url")

# Check if the response code is 200 (OK)
if [ "$response_code" == '200' ]; then
    # If the response code is 200, send a GET request and display the response body
    curl -L -s "$url"
fi
