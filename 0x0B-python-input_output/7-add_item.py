#!/usr/bin/python3
"""
Module: 7-add_item
Adds all arguments to a Python list and saves them to a file.
"""

import sys
import json
from os.path import exists

filename = "add_item.json"

# Check if the file exists
if exists(filename):
    # Load the existing list from the file
    with open(filename, "r") as file:
        my_list = json.load(file)
else:
    # Create a new empty list
    my_list = []

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
with open(filename, "w") as file:
    json.dump(my_list, file)

