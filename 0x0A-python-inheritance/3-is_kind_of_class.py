#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """function: is_kind_of_class
    returns:
        True - if obj is an instance of or if the object
         is an instance of a class that inherited from a_class
        False - if otherwise
    """

    return (isinstance(obj, a_class))
