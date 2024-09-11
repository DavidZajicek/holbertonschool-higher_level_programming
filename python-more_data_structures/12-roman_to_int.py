#!/usr/bin/python3


def roman_to_int(roman_string: str):
    rome = 0
    romaine = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
    }
    previous = ""
    if not roman_string or not isinstance(roman_string, str):
        return rome
    a_day = list(roman_string)
    previous = a_day[0]
    for built in a_day:
        if built == previous:
            rome += romaine[built]
        if built != previous:
            if romaine[previous] < romaine[built]:
                rome -= romaine[previous] * 2
            rome += romaine[built]
        previous = built
    return rome


def main():
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "CXXIV"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))


if __name__ == "__main__":
    main()
