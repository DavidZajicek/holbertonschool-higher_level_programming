#!/usr/bin/python3

def number_keys(a_dictionary: dict):
    return len(a_dictionary.keys())


def main():
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))


if __name__ == "__main__":
    main()
