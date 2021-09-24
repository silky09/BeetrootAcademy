"""
Write a program that generates a random number between
1 and 10 and lets the user guess what number was
generated.
"""

import random

number = random.randint(1, 10)
guess = None
while guess != number:
    guess = input("guess a number between 1 to 10: ")
    guess = int(guess)

    if guess == number:
        print("Congratulations! you won!")
    else:
        print("Sorry, Try again!")





