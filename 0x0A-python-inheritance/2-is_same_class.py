#!/usr/bin/python3

"""a module for a function that checks for
    the type of object passed
"""


def is_same_class(obj, a_class):
    """function: is_same_class
    returns:
            true if obj is exactly an instance of a_class
            false if otherwise
    """

    if type(obj) == a_class:
        return True
    return False
