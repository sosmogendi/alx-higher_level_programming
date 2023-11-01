#!/bin/bash
# bash script displays only the status code of the response
curl -L -s -X HEAD -w "%{http_code}" "$1"
