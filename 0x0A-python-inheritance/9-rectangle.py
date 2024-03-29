#!/usr/bin/python3
"""This defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """It represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """This Intializes a new Rectangle.

        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """This returns the print() and str() representation of a Rectangle."""
        strg = "[" + str(self.__class__.__name__) + "] "
        strg += str(self.__width) + "/" + str(self.__height)
        return strg
