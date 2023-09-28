#!/bin/bash
# This script takes a URL as an argument, sends a request using curl, and displays the body size in bytes.

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the provided URL and save the response body to a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$1"

# Get the size of the response body in bytes
body_size=$(wc -c < "$response_file")

# Display the body size
echo "$body_size"

# Clean up the temporary file
rm -f "$response_file"
