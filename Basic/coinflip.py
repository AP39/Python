from sys import exit
from random import randint
import random

Heads = 0
Tails = 0
x = 0


while x < 100000:
    coin = random.randint(1,101)
#    print(f"{coin}")


    if coin % 2 == 0:
#        print("Heads")
        Heads += 1
    else:
#        print("Tails")
        Tails += 1
    x += 1


print(f"Heads = {Heads}\nTails = {Tails}\nEnjoy.")
