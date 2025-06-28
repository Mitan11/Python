# Create a random number guessing game with python.

import random


random_number = random.randint(1, 10)

chance = 3

while chance > 0:
    num = int(input("Enter a number between 1 and 10: "))
    if num == random_number:
        print("You won!")
        break
    elif chance != 0:
        print("Try again! you have", chance, "chances left")
        chance -= 1
    else:
        print("You lost!")