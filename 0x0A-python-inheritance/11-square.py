#!/usr/bin/python3
"""This func  defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """It represents a square."""

    def __init__(self, size):
        """This initializes a new square.

        Args:
            size (int):  size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
