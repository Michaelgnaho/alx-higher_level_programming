#!/usr/bin/python3

"""This func defines a square-printing function."""


def print_square(size):
    """THIS prints a square with the # character.
    Args:
        size (int): Height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
