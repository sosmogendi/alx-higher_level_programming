#!/bin/bash
# Bash script makes a request to 0.0.0.0:5000/catch_me and displays the response
# Send the request and save the response to a temporary file
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" -o /tmp/response 0.0.0.0:5000/catch_me
# Extract and display the message from the response file
cat /tmp/response
