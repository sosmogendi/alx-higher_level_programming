#!/usr/bin/python3
"""
Module: 2-append_write
Appends a string at the end of a text file (UTF8) and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the text file. Defaults to an empty string.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
