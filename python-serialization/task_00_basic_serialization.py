#!/usr/bin/python3
"""Basic serialization module: save/load dictionary as JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Output JSON file name

    If the file exists, it will be overwritten.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): Input JSON file name

    Returns:
        dict: Python dictionary loaded from JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
