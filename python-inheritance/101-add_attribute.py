#!/usr/bin/python3
"""Module that adds a new attribute to an object if possible.
"""


def add_attribute(obj, attr_name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): Object to modify.
        attr_name (str): Attribute name to add.
        value: Value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
