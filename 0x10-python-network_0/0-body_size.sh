#!/bin/bash
# This script takes a URL as an argument, sends a request using curl, and displays the size of the response body in bytes.

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the provided URL, discard the headers, and count the bytes of the response body
body_size=$(curl -s "$1" | wc -c)

# Display the body size
echo "$body_size"
