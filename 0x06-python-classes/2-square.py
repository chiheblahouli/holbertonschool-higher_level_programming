#!/usr/bin/python3

class Square:
    """
        A Square class that will initialize and store values in it's
        private attribute __self
        Attribute:
             __size will contain the value of size
    """

    def __init__(self, size=0):
        """
            __init__ will initialize the private attribute __size with size
            size must be an integer type and > than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
