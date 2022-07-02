#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    for i in range(0, length):
       new_string = my_string.translate({ord(c): None for c in "cC"})
    return new_string
