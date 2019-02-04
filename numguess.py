#introduction
from sys import exit
from random import randint

print("\n\nWelcome to The Number Game!\n")
print("\nTry to guess what number I'm thinking, from 1 - 10. You have 5 tries\n")

#The setup.  gets number input and sets it as interger.  grabs one random number.
def game1():

    global x
    x = int(input('> '))
    global tries
    tries = 0
    global y
    y = int(randint(1, 10))
    global hint
    hint = 0

#Where the actual game takes place.
def game2():
    global x
    global tries
    global y
    global hint


    while tries < 4:

        tries += 1

        if tries == 3 and hint == 0 and x != y:
            print("You have two quess left, would you like a hint?")
            hint = input("press '99' for hint, press 88 for no hint.")
#            hint1 = int(hint)
            if hint == '99':
                hintbot()
            else:
                tries -= 1
                hint = 1
                game2()
        if x == y:
            print(f"You got it!  The number was {y}.")
            exit(0)

        if x != y:
            print(f"Sorry, {x} is wrong, try again.")
            #test
#            print(f"NUMBER IS {y}.")
            #test
            x = int(input(f'Try again. You\'ve guessed {tries} time(s).\n> '))
        if tries >= 4 and x != y:
            print(f"YOU LOSE!\nThe number was {y}!\nGAME OVER!")
            exit(0)
        if tries >= 4 and x == y:
            print(f"You got it!  The number was {y}.")
            exit(0)
#later integration of hinbot is numbers get bigger
def hintbot():
    global y
    global x
    global tries
    global hint

    if x < y:
        print("\nGuess HIGHER!")
        hint = 1
        tries -= 1
        input('> ')
        game2()
    if x > y:
        print("\nGuess LOWER!")
        hint = 1
        tries -= 1
        input('> ')
        game2()

game1()
game2()
