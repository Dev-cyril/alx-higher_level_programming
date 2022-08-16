#!/usr/bin/python3

'''
    Implementing a Rectangle class
'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """defining the rectangle class"""
    def __init__(self, size):
        """initializing the instances"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculating area"""
        return self.__size * self.__size

    def __str__(self):
        """print statement"""
        return("[Square] {}/{}".format(str(self.__size), str(self.__size)))
