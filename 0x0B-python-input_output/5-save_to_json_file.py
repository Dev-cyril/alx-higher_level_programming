#!/usr/bin/python3

"""a module for saving into file using json"""


import json


def save_to_json_file(my_obj, filename):
    """fuction: save_to_json_file
    writes an object into a file using json representation
    Args:
        my_obj - an object
        filename - path to file
    returns:
        None
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
