#!/usr/bin/python3

def uppercase(string: str):
    for c in string:
        if ord(c) >= 97 and ord(c) <= 122:
            c -= 32
