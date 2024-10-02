#!/usr/bin/python3
"""
6. Create object from a JSON file
mandatory
Write a function that creates an Object from a “JSON file”:
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    for arg in sys.argv[1:]:
        data.append(arg)

    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    main()
