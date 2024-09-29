#!/usr/bin/python3
"""
4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
mandatory
Arf, Bark, Meow
"""


class Fish:
    def swim(self):
        print('The fish is swimming')

    def habitat(self):
        print('The fish lives in water')


class Bird:
    def fly(self):
        print('The bird is flying')

    def habitat(self):
        print('The bird lives in the sky')


class FlyingFish(Bird, Fish):
    def fly(self):
        print('The flying fish is soaring!')

    def swim(self):
        print('The flying fish is swimming!')

    def habitat(self):
        print('The flying fish lives both in water and the sky!')


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())
