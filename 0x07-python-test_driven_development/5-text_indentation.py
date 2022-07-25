#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == ' ':
            continue
        if i == '.' or i == '?' or i == ':':
            print(i)
            print()
        else:
            print(i, end='')
