#!/usr/bin/python3
"""
Module for serializing and deserializing Python dictionaries to/from XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML and save to a file."""
    def build_element(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, str(key))
                build_element(child, value)
        elif isinstance(data, list):
            for item in data:
                item_elem = ET.SubElement(parent, "item")
                build_element(item_elem, item)
        else:
            parent.text = str(data)

    root = ET.Element("data")
    build_element(root, dictionary)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file back into a Python dictionary."""
    def parse_element(element):
        # If element has no children, parse value
        if not list(element):
            text = element.text
            if text is None:
                return None
            text = text.strip()
            if text.lower() == "true":
                return True
            elif text.lower() == "false":
                return False
            else:
                try:
                    if "." in text:
                        return float(text)
                    return int(text)
                except ValueError:
                    return text
        # If element has children, check if it's a list or dict
        children = list(element)
        # If all children are "item", treat as list
        if all(child.tag == "item" for child in children):
            return [parse_element(child) for child in children]
        # Otherwise, treat as dict
        return {child.tag: parse_element(child) for child in children}

    tree = ET.parse(filename)
    root = tree.getroot()
    return parse_element(root)

