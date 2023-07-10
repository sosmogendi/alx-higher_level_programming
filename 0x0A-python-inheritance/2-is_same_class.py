#!/usr/bin/python3

"""
2-is_same_class module

This module contains the `is_same_class` function that checks if an object is exactly
an instance of the specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: An object to be checked.
        a_class: A class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        False otherwise.
    """
    return type(obj) is a_class
