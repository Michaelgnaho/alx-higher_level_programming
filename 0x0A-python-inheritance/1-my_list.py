#!/usr/bin/python3
"""This defines an inherited list class MyList."""


class MyList(list):
    """It prepares a sorted printing for the built-in list class."""

    def print_sorted(self):
        """ It print a list in sorted ascending order."""
        print(sorted(self))
