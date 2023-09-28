#!/bin/bash
# sends a GET request to the URL
# Check if a URL argument is provided
target_url="$1"

if [ $(curl -L -s -X HEAD -w "%{http_code}" "$target_url") == '200' ]; then
    curl -Ls "$target_url"
fi
