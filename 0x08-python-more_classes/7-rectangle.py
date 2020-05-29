#!/usr/bin/python3
""" Rectangle class with width and height.
It can return perimeter and area values.
If width or height is equal to 0, return an empty string.
Also__repr__ represents the rectangle and delete it.
The number of intances of rectangle is calculated.
"""


class Rectangle:
    """ Rectangle class with width, height, area, perimeter
    and an empty string.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for height in range(self.__height):
            str += str(self.print_symbol)
            for width in range(self.__width - 1):
                str += str(self.print_symbol)
            if height < self.__height - 1:
                str += "\n"
        return str

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)
