#!/usr/bin/python3

def update_dictionary(a_dictionary: dict, key, value):
    a_dictionary.update({key: value})
    return a_dictionary


def main():
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    update_dictionary(a_dictionary, 'language', "Python")


if __name__ == "__main__":
    main()
