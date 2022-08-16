#!/usr/bin/python3

def is_same_class(obj, a_class):
    """function: is_same_class
    returns:
            true if obj is exactly an instance of a_class
            false if otherwise
    """

    if type(obj) == a_class:
        return True
    return False
