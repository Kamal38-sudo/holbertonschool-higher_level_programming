#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle.

The Square class includes:
- private size validated as a positive integer
- area() method
- __str__ method inherited from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize Square with private size."""
        self.integer_validator("size", size)
        self.__size = size
        # Call the Rectangle constructor with width and height equal to size
        super().__init__(size, size)
