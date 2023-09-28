#!/bin/bash
# This script takes a URL as an argument and displays the allowed HTTP methods

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract the URL from the command-line argument
url="$1"

# Use curl to send an HTTP OPTIONS request to the URL and display the allowed methods
curl -sI -X OPTIONS "$url" | grep "Allow" | cut -d ' ' -f 2-
