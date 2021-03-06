#!/usr/bin/python3
"""
define a class Square
"""


class Square():
    """ A class square """
    def __init__(self, size=0):
        """ Initializing """
        self.__size = size

    @property
    def size(self):
        """ Proper size """
        return self.__size

    @size.setter
    def size(self, value):
        """ property better size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Initializing area calculation """
        return self.__size * self.__size

    def my_print(self):
        """ Initializing printing """
        if self.__size <= 0:
            print()

        else:
            print(((("#" * self.__size) + '\n') * self.__size), end="")
