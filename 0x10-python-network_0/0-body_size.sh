#!/bin/bash
# This script takes a URL as an argument, sends a request using curl, and displays the body size in bytes.

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the provided URL and capture the response
response=$(curl -sI "$1")

# Extract the Content-Length header value (body size) from the response headers
body_size=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}')

# Check if Content-Length header was found
if [ -z "$body_size" ]; then
    echo "Unable to determine body size for this URL."
    exit 1
fi

# Display the body size
echo "$body_size"
