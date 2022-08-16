#!/usr/bin/python3

"""A read_file module"""


def read_file(filename=""):
    """A function that takes a file and either reads or write into
     or appends text into the file when opened
     Args: path to file
    """

    with open(filename, encoding='utf-8') as txt:
        content = txt.read()
        print(content)
