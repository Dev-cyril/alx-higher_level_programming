#!/usr/bin/python3

"""A class `Square` that inherits from rectangle.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class: Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """string representation of the class"""
        return"[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.__size)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value <= 0:
                raise ValueError("size must be > 0")
            else:
                self.__size = value
                self.width = self.height = value

    def update(self, *args, **kwargs):
        """updates arguments of an attribute"""
        actual = (self.id, self.size, self.x, self.y)
        if len(args) != 0:
            self.id, self.size, self.x, self.y = \
                args + actual[len(args):len(actual)]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of the class"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
