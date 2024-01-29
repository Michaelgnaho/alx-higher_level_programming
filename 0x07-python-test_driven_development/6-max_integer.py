#!/usr/bin/python3
"""This module finds the max integer in a list
"""


def max_integer(list=[]):
    """This function finds and returns the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    it = 1
    while it < len(list):
        if list[it] > result:
            result = list[it]
        it += 1
    return
