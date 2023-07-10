#!/usr/bin/python3
"""
Module 11-square

A module that contains the definition of a Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
