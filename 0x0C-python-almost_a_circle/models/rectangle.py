#!/usr/bin/python3
""" Rectangle Module """

from models.base import Base


class Rectangle(Base):

    """ Rectangle class inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display the Rectangle using '#' character """
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ Return a string representation of the Rectangle """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
    - {self.width}/{self.height}"

    def display(self):
        """ Display the Rectangle using '#' character """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Update the attributes of the Rectangle """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the Rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }