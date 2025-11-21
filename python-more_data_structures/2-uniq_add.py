#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0
    for x in my_list:
        if x not in unique:
            unique.append(x)
            total += x
    return total
