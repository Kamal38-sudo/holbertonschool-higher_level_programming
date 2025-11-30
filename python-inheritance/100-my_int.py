#!/usr/bin/python3
"""MyInt class module.
"""


class MyInt(int):
    """Rebel integer class with inverted == and != operators."""

    def __eq__(self, other):
        """Invert equality: == returns False if values are equal."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Invert inequality: != returns True if values are equal."""
        return not super().__ne__(other)
