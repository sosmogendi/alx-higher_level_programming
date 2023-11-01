#!/bin/bash
# script encoding for a URL-encoded POST request
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
