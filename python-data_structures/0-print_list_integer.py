#!/usr/bin/python3
def print_list_integer(my_list=[1, 2, 3, 4, 5]):
    """Print all integers of a list, one per line using str.format()"""
    for num in my_list:
        print("{}".format(num))
print_list_integer()
