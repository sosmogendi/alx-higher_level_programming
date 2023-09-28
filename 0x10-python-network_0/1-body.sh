#!/bin/bash
# This script takes a URL as an argument, sends a GET request using curl, and displays the body of the response for a 200 status code.

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the provided URL and follow redirects (-L), then display the response body
curl -sL "$1"
