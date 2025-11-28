#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and deserialization."""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes in this list are retrieved.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
