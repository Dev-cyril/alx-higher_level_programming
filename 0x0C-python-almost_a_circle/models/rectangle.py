#!/usr/bin/python3

"""A class module that inherits from the base file"""


from models.base import Base


class Rectangle(Base):
    """class: Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """getter of self.__width
            returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """getter of self.__width
            returns the value of width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """getter of self.__width
            returns the value of width
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """getter of self.__width
            returns the value of width
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """calculates the area of the rectangle class"""

        return(self.__width * self.__height)

    def display(self):
        """method that prints a rectangle shape"""
        print("\n" * self.__y)
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Method that assigns arguments to each attribute"""
        actual = (self.id, self.width, self.height, self.x, self.y)
        if len(args) != 0:
            self.id, self.width, self.height, self.x, self.y = \
                args + actual[len(args):len(actual)]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the class"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
