#!/usr/bin/python3

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

