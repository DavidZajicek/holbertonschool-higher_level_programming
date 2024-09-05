#!/usr/bin/python3

def fizzbuzz():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz".format(), end=" ")
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz".format(), end=" ")
        if i % 3 != 0 and i % 5 == 0:
            if i == 100:
                print("Buzz".format())
            else:
                print("Buzz".format(), end=" ")
