#!/usr/bin/python3

class LockedClass:
    """
    Class that prevents the dynamic creation of new instance attributes, except for 'first_name'.
    """

    def __setattr__(self, name, value):
        if name != 'first_name' or hasattr(self, name):
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
