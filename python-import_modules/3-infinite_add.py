#!/usr/bin/python3
import sys


def main():
    result = 0
    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
    print("{}".format(result))


if __name__ == "__main__":
    main()
