#!/bin/bash

# Send a POST request to the specified URL with the required headers
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
