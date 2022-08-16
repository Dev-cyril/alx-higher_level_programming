#!/usr/bin/python3

"""A write_file module"""


def write_file(filename="", text=""):
    """A function that writes into a file
    Arg:
        filename - path to file
        text - content to write into the file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        txt = f.write(text)
        return(txt)
