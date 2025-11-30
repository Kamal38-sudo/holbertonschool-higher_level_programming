#!/usr/bin/python3
"""Student class module.
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    If None, all attributes are retrieved.

        Returns:
            dict: Dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__.copy()
        new_dict = {}
        for key in attrs:
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict

