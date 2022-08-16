#!/usr/bin/python3

"""a module that checks if an object is an
    instance of an object
"""



def is_kind_of_class(obj, a_class):
    """function: is_kind_of_class
    returns:
        True - if obj is an instance of or if the object
         is an instance of a class that inherited from a_class
        False - if otherwise
    """

    return (isinstance(obj, a_class))
