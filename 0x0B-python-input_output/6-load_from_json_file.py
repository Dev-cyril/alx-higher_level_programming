#!/usr/bin/python3

"""a module for creating an object from json file"""


import json


def load_from_json_file(filename):
    """A function that creates an object from a json file.
    Args -
        filename:  path to file
    """

    with open(filename, encoding='utf-8') as f:
        return json.load(f)
