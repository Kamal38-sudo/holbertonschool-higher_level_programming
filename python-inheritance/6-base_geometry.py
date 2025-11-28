#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Public instance method that raises an Exception."""
        raise Exception("area() is not implemented")
