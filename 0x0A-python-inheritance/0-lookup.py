#!/usr/bin/python3

"""
0-lookup.py:
This module provides a function to return a list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of attributes and methods.

    """
    return dir(obj)
