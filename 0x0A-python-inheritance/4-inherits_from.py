#!/usr/bin/python3

"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: An object to be checked.
        a_class: A class to compare against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
