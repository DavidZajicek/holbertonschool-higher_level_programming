#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for (k, d) in dictionary.items():
        ET.SubElement(root, k).text = d

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        if child.tag == 'age':
            data[child.tag] = int(child.text)
        else:
            data[child.tag] = child.text
    return data


if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
