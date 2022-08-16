#!/usr/bin/python3

class BaseGeometry:
    """A class that perfoms a basic geometry"""

    def area(self):
        """Calculates the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value type
        Args:
            name - a string
            value - an integer
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
