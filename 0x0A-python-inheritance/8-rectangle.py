#!/usr/bin/python3

'''
    Implementing a Geometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle class"""

    def __init__(self, width, height):
        """Instantiate the class instances"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
