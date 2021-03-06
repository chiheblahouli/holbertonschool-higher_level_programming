#!/usr/bin/python3
"""
define a class Square
"""


class Square:
    """a class Square that defines as a square"""
    def __init__(self, size=0):
        """instantiation with size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
