#!/usr/bin/python3
"""
Module: 8-class_to_json
Contains a function for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Serializes an object to a dictionary representation for JSON serialization.
    """

    return obj.__dict__
