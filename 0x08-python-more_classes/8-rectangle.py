#!/usr/bin/python3
""" Rectangle class with width and height.
It can return perimeter and area values.
If width or height is equal to 0, return an empty string.
Also__repr__ represents the rectangle and delete it.
The number of instances of rectangle is calculated.
Public class attribute print_symbol.
def bigger_or_equal compares 2 rectangle and returns the biggest one
"""


class Rectangle:
    """ Rectangle class with width, height, area, perimeter
    and an empty string. Adding print_symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return str1
        for height in range(self.__height):
            str1 += str(self.print_symbol)
            for width in range(self.__width - 1):
                str1 += str(self.print_symbol)
            if height < self.__height - 1:
                str1 += "\n"
        return str1

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2
