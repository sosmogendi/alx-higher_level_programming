#!/usr/bin/python3
"""
Module containing the Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a farewell message when an instance of Rectangle is deleted
        and decrements the number_of_instances attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
