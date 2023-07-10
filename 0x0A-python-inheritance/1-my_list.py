#!/usr/bin/python3

"""
This module defines the MyList class, which is a custom list class
that inherits from the built-in list class.
"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public instance method:
    - print_sorted(self): Prints the list in sorted order (ascending sort).
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).

        Args:
            None
        
        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
