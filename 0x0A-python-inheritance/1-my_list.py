#!/usr/bin/python3

class MyList(list):
    """function: MyList
    returns: nothing
    """

    def print_sorted(self):
        """sorts lists and prints the result"""

        print(sorted(self))
