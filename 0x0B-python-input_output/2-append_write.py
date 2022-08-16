#!/usr/bin/python3

def append_write(filename="", text=""):
    """A function that appends text to the end of a file
    Arg:
        filename - path to file
        text - content to write into the file
    """

    with open(filename, 'a', encoding='utf-8') as f:
        txt = f.write(text)
        return(txt)
