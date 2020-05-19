#!/usr/bin/python3
"""
    documentation of the module square
"""


class Square:
    """ A class square """
    def __init__(self, size=0):
        """ Initializing """
        self.__size = size


    @property
    def size(self):
        """ defining size """
        return self.__size

    @size.setter
    def size(self, value):
        """ definiting size better"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Initializing area """
        return self.__size * self.__size
