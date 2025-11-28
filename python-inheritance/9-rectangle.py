#!/usr/bin/python3
"""
Module 9-rectangle
Defines a Rectangle class that inherits from BaseGeometry.

The Rectangle class includes:
- private width and height validated as positive integers
- area() method
- __str__ method returning [Rectangle] <width>/<height>
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

