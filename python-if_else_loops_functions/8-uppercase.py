#!/usr/bin/python3

def uppercase(string: str):
    s = list(string)
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
    print("".join(s).format())
