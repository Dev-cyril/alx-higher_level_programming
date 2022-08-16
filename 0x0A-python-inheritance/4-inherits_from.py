#!/usr/bin/python3

def inherits_from(obj, a_class):
    """function: inherits_from
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    return:
        True - if the object is an instance of a class that inherited
                (directly or indirectly) from the specified class
        False - if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
