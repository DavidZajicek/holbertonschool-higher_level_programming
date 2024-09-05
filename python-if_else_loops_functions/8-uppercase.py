#!/usr/bin/python3

def uppercase(string: str):
    s = list(string)
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            s[i] = chr(ord(s[i]) - 32)
    print("".join(s).format())
