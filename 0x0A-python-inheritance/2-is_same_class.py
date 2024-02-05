#!/usr/bin/python3
"""This defines a class-checking function."""


def is_same_class(obj, a_class):
    """ It checks if an object is exactly an instance of a given class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        True, If obj is exactly an instance of a_class 
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
