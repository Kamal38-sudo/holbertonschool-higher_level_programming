#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the list itself.
        """
        print(sorted(self))

