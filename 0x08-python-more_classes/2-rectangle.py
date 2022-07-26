#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle
        Args:
            width(int): width of the rectangle
            height (int): height of the rectangle
        Returns:
            None
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter of __width
        Returns:
            the value of the rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width
        Args:
            value (int): takes the width of the rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """getter of __height
        Returns:
            the value of the rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            value (int): takes the height of the rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """calculates the area of the rectangle
        Returns:
            The area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """calculates the perimeter of the rectangle
        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return(2 * (self.__width + self.__height))
