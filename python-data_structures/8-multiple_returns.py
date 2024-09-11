#!/usr/bin/python3

def multiple_returns(sentence: str):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])


def main():
    sentence = ""
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))


if __name__ == "__main__":
    main()
