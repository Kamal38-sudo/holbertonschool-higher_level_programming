#!/usr/bin/python3
"""Module that defines a function to convert a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure for JSON serialization of obj."""
    return obj.__dict__.copy()
