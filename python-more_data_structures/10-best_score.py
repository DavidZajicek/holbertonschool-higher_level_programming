#!/usr/bin/python3


def best_score(a_dictionary: dict):
    if not a_dictionary:
        return None
    top = list(a_dictionary)[0]
    for i, v in a_dictionary.items():
        if v > a_dictionary[top]:
            top = i
    return top


def main():
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))


if __name__ == "__main__":
    main()
