#!/usr/bin/python3
"""THis defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """It represents a square."""

    def __init__(self, size):
        """It initializea a new square.

        Args:
            size (int): size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
