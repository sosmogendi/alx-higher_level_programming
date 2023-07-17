#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update the attributes of the Square """
        super().update(*args, **kwargs)
