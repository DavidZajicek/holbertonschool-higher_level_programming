#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
import csv
import json


def convert_csv_to_json(csv_file):
    objects = []

    try:
        with open(csv_file, encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                objects.append(row)

    except FileNotFoundError:
        return False

    with open('data.json', 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(objects))

    return True


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
