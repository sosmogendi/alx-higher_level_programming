#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Print the square using the character #."""
        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        square_s = ""
        if self.size == 0:
            return square_s
        square_s += "\n" * self.position[1]
        square_s += "\n".join((" " * self.position[0] + "#" * self.size)
                                for _ in range(self.size))
        return square_s

