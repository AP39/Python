from sys import exit
from random import randint
import time
global name
global op
"""
This is a simple turn-based fighting game that allows you to face off against the computer in a fight to the death.
"""

global str
global opstr
str = 100
opstr = 100

print("\n\nWELCOME TO PYTHON FIGHT!!!\n\n")

name = input("What is your fighter's name?\n>")
op = input("What is your opponents fighter's name?\n>")

print(f"\nTODAY!!!\n\nWe have a fight between {name} and {op}!!!!!\n\nEach fighter will take turns and at the end we will have one winner!")

print(f"\nYou can choose, {name}, between a punch or a kick.  \nSo can your opponent. The fighter still standing at the end will win!")



print(f"You can go first {name}.\nLETS FIGHT!!\n")

def fight():
    global str
    global opstr
    global name
    global op

    if str > 1 and opstr > 1:
#        print(f"\n{op} has {opstr} power and {name} has {str} power.\n")
        move = input("Will you punch or kick.\n>")
        if move == "punch":
            y = int(randint(1, 10))
            print(f"You punched {op} with a power of {y}\n")
            opstr = opstr - y
            fight2()
        elif move == "kick":
            y = int(randint(1, 20))
            print(f"You kicked {op} with a power of {y}\n")
            opstr = opstr - y
            fight2()
        elif move == "special" or "s":
            y = int(randint(1, 100))
            print(f"You SPECIALLED {op} with a power of {y}\n")
            opstr = opstr - y
            fight2()
        else:
            print("I said punch or kick...  You lose a turn...\n")
            time.sleep(1)
            fight2()

    else:
        ending()

def fight2():
    global str
    global opstr
    global name
    global op

    if str > 1 and opstr > 1:
        opmove = int(randint(1,11))


        if opmove > 5:
            print(f"{op} punched you with a power of {opmove}")
            str = str - opmove
            print(f"\n{op} has {opstr} power and {name} has {str} power.\n")
            fight()

        else:
            y = int(randint(1, 15))
            print(f"{op} kicked you with a power of {opmove}")
            str = str - opmove
            print(f"\n{op} has {opstr} power and {name} has {str} power.\n")
            fight()

    else:
        ending()




def ending():
    global str
    global opstr
    global name
    global op

    if str > 0:

        print(f"\nThe fight is now over {name} had {str} power and {op} is dead.\n")

    else:

        print(f"\n{name} is dead and {op} has {opstr} power remaining.\n")

    again = input("Do you want to fight again??? y or n\n> ")

    if again == 'y':
        print("\n\nWELCOME TO PYTHON FIGHT!!!\n\n")
        name = input("What is your fighter's name?\n>")
        op = input("What is your opponents fighter's name?\n>")
        str = 100
        opstr = 100
        fight()

    else:
        print("Ok, BYE!")
        exit(0)

fight()
