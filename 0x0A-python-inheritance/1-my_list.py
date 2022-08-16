#!/usr/bin/python3

""" a class module that sorts a list"""


class MyList(list):
    """function: MyList
    returns: nothing
    """

    def print_sorted(self):
        """sorts lists and prints the result"""

        print(sorted(self))
