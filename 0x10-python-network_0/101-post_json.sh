#!/bin/bash
# Bsh script for posting JSON data files and testing a server
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
