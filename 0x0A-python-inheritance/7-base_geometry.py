#!/usr/bin/python3
"""This defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This reprsents base geometry."""

    def area(self):
        """if not  implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ It validates a parameter as an integer.

        Args:
            name (str):  name of the parameter.
            value (int):  parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
