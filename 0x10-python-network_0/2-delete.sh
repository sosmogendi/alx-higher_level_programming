#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response.

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a DELETE request to the provided URL and display the response body
curl -s -X DELETE "$1"
