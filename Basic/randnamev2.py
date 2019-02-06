"""
This program takes an input of a 2 letter string from the user.  There are 2 monkies that will type lowercase letters at random and try to guess or match your
string.  The program will record the number of guesses the monkies take with a maximum of 900.
"""
import random
import string
global a
global c
global cc
global ccc
global guess
import time
c = 0
cc = 0

a = input("\nChoose a 2 letter lowercase string for the 2 monkies to try to guess.\n> ")

#takes the user's 2 letter string and gives it to the first monkey
def monkey():
    global c
    global cc
    global ccc
    global a

    w = random.choice(string.ascii_lowercase)
    x = random.choice(string.ascii_lowercase)
#    y = random.choice(string.ascii_lowercase)
#    z = random.choice(string.ascii_letters)
    guess = w + x


    if a != guess:


        if c < 450:
            c += 1
            monkey()

        else:
            print(f"Sorry, the first monkey didn't guess \"{a}\" in {c} tries, bad monkey, let's try another monkey...\n")
            time.sleep(1)
            monkey2()

    else:
        ccc = c + cc
        print(f"\nTHE FIRST MONKEY GUESSED {a} IN {c} TRIES!")
#        print(f"It took the monkeys {ccc} tries to guess \"{a}\".\n")
#        repeat()

#if the first monkey fails in 450 attempt the same user input is passed to the second monkey
def monkey2():
    global c
    global cc
    global ccc
    global a


    ww = random.choice(string.ascii_lowercase)
    xx = random.choice(string.ascii_lowercase)
#    y = random.choice(string.ascii_lowercase)
#    z = random.choice(string.ascii_letters)
    guess2 = ww + xx


    if a != guess2:


        if cc < 450:
            cc += 1
            monkey2()

        else:
            ccc = c + cc
            print(f"Sorry, the second monkey didn't guess \"{a}\" it in {cc} tries...\n")
            print(f"The monkeys failed to guess \"{a}\" after {ccc} tries...\n")
            cc = 0
            time.sleep(1)
#            repeat()

    else:
        ccc = c + cc
        print(f"\nTHE SECOND MONKEY GUESSED \"{a}\" IN {cc} TRIES!")
        print(f"It took the monkeys {ccc} tries to guess \"{a}\".\n")
#        repeat()

def repeat():
    global a
    global c
    global cc
    global ccc
    z = input("Do you want to try again?? y or n\n> ")

    if z == 'y':
        c = 0
        cc = 0
        ccc = 0
        a = input("\nChoose a 2 letter lowercase string for the 2 monkies to try to guess.\n> ")
        monkey()
    else:
        print("\nOK! BYE!\n")
        exit(0)

monkey()
print("\nOK! BYE!\n")
