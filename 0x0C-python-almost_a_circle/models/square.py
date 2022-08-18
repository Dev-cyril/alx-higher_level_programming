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
    def size(self) -> int:
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """size setter"""
        self.__size = value
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """updates arguments of an attribute"""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of the class"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
