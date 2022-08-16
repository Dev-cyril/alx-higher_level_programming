#!/usr/bin/python3

""" Module for lookup function
which returns a list
"""


def lookup(obj):
    """ function: lookup
    Return: list of available methods of obj
    """

    return dir(obj)
