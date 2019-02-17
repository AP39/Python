""" This program allows the user to bet on a python race where 3 pythons race to
    the finish line.  Players can keep betting on races until they rin out of
    money and are kicked out of the python racing trackself.
"""
from sys import exit
from random import randint
import random
import time

print("\nWelcome to Python Race.")
money = 100000

def start(money):
    time.sleep(2)
    Pythons = [
                'Billy Billy', 'Slow Pete', 'Tiny Lou',
                'Big Zeke', 'Lil Money Maker', 'Ace',
                'NZ Special', 'American Wonder', 'Forest Slither',
                'Electric Avenue', 'Turbo Mama', 'Lightning Tubby',
                'Big Lou', 'Lazer', 'Blazer', 'Sir Alexander',
                'African King', 'Plop', 'Maximumo',
                'Sweet Baby Mick'
            ]
    tempPythons = Pythons.copy()
    current_racers = {}
    racers = int(len(tempPythons))
    count = 1

    while count < 4:
        y = int(randint(1, racers))
        x = y - 1
        stable = tempPythons[x]
        try:
            current_racers[stable] = int(randint(60, 101))
            tempPythons.pop(x)
            count += 1
        except IndexError:
            print("One of the pythons quit do to a prior engagement, lets try again.")
            start(money)    

    tempPythons.clear()
    stable = []
    print("\nToday's racing pythons are:")
    for python, power in current_racers.items():
        print(python)

    time.sleep(2)
    bank = 0
    bet_count = 1
    race_list = []

    if money > 0:
        print(f"\nPlace your bets!!! You have ${money} in your wallet.")

    else:
        print("Sorry, you dont have any money and were kicked out of the track.")
        exit(0)

    for python, power in current_racers.items():
        print(f"To bet on '{python}' press {bet_count}")
        race_list.append(python)
        bet_count += 1

    bet_choice = int(input("> ")) - 1

    if bet_choice == 0 or bet_choice == 1 or bet_choice == 2:
        print(f"\nYou chose {race_list[bet_choice]}")
        bet_choice = race_list[bet_choice]

    else:
        print("You were beat up and thrown out of the track because you cant type 1, 2 or 3, you were also robbed...")
        money = money - 12000
        start(money)

    bet_amount = int(input(f"How much would you like to bet?\nYou have ${money}.\n> "))

    if bet_amount < 0:
        print("You cant bet negative, duh. You were robbed and kicked out...")
        money = money - 17000
        bet_amount = 0
        start(money)

    elif bet_amount > money:
        print("You dont even have that much and someone robbed you and you were kicked out...")
        money = money - 14000
        bet_amount = 0
        start(money)

    else:
        print(f"OK! You bet ${bet_amount}!\n")
        money = money - bet_amount
        bank = bank + bet_amount
        bet_amount = 0

    print("AND WE'RE READY!!!")
    time.sleep(.5)
    print("On your marks...")
    time.sleep(.5)
    print("Get Set...")
    time.sleep(.5)
    print("GO!!!")
    time.sleep(2)

    print("At the half way mark, \n")
    current_racers2 = current_racers.copy()
    position = ['first', 'second', 'third']
    pos = 0
    for p in sorted(current_racers, key=current_racers.get, reverse=True):

        print(f"{p} is in {position[pos]} place!")
        pos += 1
        current_racers[p] = int(randint(60, 101)) + current_racers2[p]

    time.sleep(4)
    print("\nTHEY'RE ROUNDING THE FINAL CORNER")
    time.sleep(.5)
    print("HERE THEY COME!")
    time.sleep(.5)
    print("AND THE RESULTS ARE IN!!!\n\n")
    time.sleep(2)

    pos = 0
    for p in sorted(current_racers, key=current_racers.get, reverse=True):

        print(f"{p} finished the race in {position[pos]} place!")
        pos += 1

    current_racers2 = sorted(current_racers, key=current_racers.get, reverse=True)
    print(f"\nAnd the winner is... {current_racers2[0]}!!!")
    time.sleep(1)
    winner = current_racers2[0]
    if bet_choice == winner:
        print(f"\nYou picked the right python!!!  You won ${bank * 5}!!!")
        money = money + bank * 5
        bank = 0

    else:
        print(f"You picked the wrong python.\nYou lost ${bank}...")
        bank = 0

    if money <= 0:
        print("Sorry, you dont have any money and were kicked out of the track.\nBYE!")
        exit(0)

    again = input("Would you like to bet again? 'y' or 'n'\n> ")
    if again == 'y':
        start(money)
    else:
        print("Ok, BYE!")
        exit(0)

start(money)
