#!/usr/bin/python3

for i in range(97, 123):
    if i != 113 and i != 101:
        print(chr(i).format(i), end="")
