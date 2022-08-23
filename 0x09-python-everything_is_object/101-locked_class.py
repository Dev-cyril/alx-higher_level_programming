#!/usr/bin/python3
"""A lockedClass class"""


class LockedClass:
    """class definition"""

    def __setattr__(self, attr, value):
        """Attribute setting
            Args:
                attr - attribute to be set
                value - attribute's value
        """

        if attr != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute \
                    '{}'".format(attr))
        self.__dict__.update({attr: value})
