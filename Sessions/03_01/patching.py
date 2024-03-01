import random


def greet():
    print("Hello, World")


def check():
    luck = random.random()
    if luck < 0.5:
        print("Sorry")
    else:
        print("Congratulations")
