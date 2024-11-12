#!/usr/bin/python3
"""
0. Generate Invitations
mandatory
Write a function that generates invitations
"""
import os
import sys


class Attendee(dict):
    def __missing__(self, key):
        return "N/A"

    def __getitem__(self, key):
        return super().__getitem__(key) or "N/A"


def generate_invitations(template: str, attendees: [dict]):
    """
    Generate Invitations
    """
    index = 1
    if not isinstance(template, str):
        print(f"Expected: str Received: {type(template)}")
        sys.exit()
    if not isinstance(attendees, list):
        print(f"Expected: str Received: {type(attendees)}")
        sys.exit()
    if len(attendees) < 1:
        print("No data provided, no output files generated.")
        return
    if not isinstance(attendees[0], dict):
        print("Attendees data must be a list of dictionaries")
        return
    if template == "":
        print("Template is empty, no output files generated.")
        return

    for attendee in attendees:
        try:
            output = template.format_map(Attendee(**attendee))
            if os.path.exists(f"output_{index}.txt"):
                raise FileExistsError
            with open(f"output_{index}.txt", 'w') as file:
                file.write(output)
            file.close()
            index += 1
        except FileExistsError as exc:
            print(exc)
        # print(output)


if __name__ == "__main__":
    # Read the template from a file
    with open('template.txt', 'r') as _file:
        template_content = _file.read()

    # List of attendees
    _attendees = [
        {"name": "Alice", "event_title": "Python Conference",
            "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
            "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"non-existing-key": "unused-value"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, _attendees)
