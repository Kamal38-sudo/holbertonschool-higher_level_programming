#!/usr/bin/python3
"""Module that defines a function to append a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF-8) and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
