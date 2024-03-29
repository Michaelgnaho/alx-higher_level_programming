#!/usr/bin/python3
"""This defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """It checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        True, If obj is an instance or inherited instance of a_class.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
