#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list sorted without modifying the original list.
        """
        print(sorted(self))
