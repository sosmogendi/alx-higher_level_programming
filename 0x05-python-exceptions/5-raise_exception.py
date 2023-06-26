#!/usr/bin/python3

def raise_exception():
    try:
        1 + 'eight'  # Attempting an operation that raises a TypeError
    except TypeError:
        raise

