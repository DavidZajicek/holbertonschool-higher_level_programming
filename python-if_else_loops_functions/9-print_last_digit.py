#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        print("{}".format(number % -10), end="")
        return number % -10
    elif number > 0:
        print("{}".format(number % 10), end="")
        return number % 10
    print("0".format(), end="")
    return 0
