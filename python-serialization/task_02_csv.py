#!/usr/bin/python3
"""Module to convert CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and save to data.json.

    Args:
        csv_filename (str): Path to the input CSV file

    Returns:
        bool: True if successful, False if an error occurs
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True
    except Exception:
        return False
