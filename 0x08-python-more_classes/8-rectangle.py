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
    number_of_instances = 0
    print_symbol = '#'

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

    def __str__(self):
        """returns the string representation of the Rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns the formal string representatiion of the instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when a deleted instance is called"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that returns the maximum value between two rectangles' area
        Returns:
            rect_1: if rect_ is greater or equal to rect_2
            rect_2: if rect_2 is greater
        """
        
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area() or rect_1 == rect_2:
            return rect_1
        return rect_2
