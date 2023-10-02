#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__hight = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__hight

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("hight must be an integer")
        if value < 0:
            raise ValueError("hight must be >= 0")
        self.__hight = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__hight * self.__width

    def perimeter(self):
        return 2*(self.height + self.__width)
