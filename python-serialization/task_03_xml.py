import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    """
    root = ET.Element("data")  # XML root element

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)  # XML only stores strings

    # Create XML tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for elem in root:
        value = elem.text

        # Try converting back to int or float if possible
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except (ValueError, TypeError):
                pass  # keep as string if not number

        result[elem.tag] = value

    return result


# Test the functions (optional)
if __name__ == "__main__":
    sample_dict = {
        "name": "Alice",
        "age": 25,
        "height": 1.68,
        "city": "Paris"
    }

    serialize_to_xml(sample_dict, "data.xml")
    restored = deserialize_from_xml("data.xml")

    print("Deserialized dictionary:", restored)

