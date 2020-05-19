#!/usr/bin/python3
class Square():
    """ A square """
    def __init__(self, size=0):
        """ Initializing """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
