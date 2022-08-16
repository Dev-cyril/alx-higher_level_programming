#!/usr/bin/python3

"""a json module for data representation"""


import json


def from_json_string(my_str):
    """function - from_json_string
    Arg:
        my_str - any object literal
    Return:
        an object (Python data structure) represented by a JSON string
    """

    return json.loads(my_str)
