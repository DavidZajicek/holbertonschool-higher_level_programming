#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print("0 arguments.".format())
    if len(sys.argv) == 2:
        print("1 argument:".format())
        print("1: {}".format(sys.argv[1]))
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
