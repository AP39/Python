"""
    This app allows the user to roll as many dice as they like.  It can print out
    as many or few rolls as wanted.  It also shows the amount of each number
    rolled and shows statistics on the total amount of rolls.
"""

from random import randint

print("Welcome to DiceMan\n")


def dice_roll():

    dice_rolls = 0
    dice_results = []
    dice = [1, 2, 3, 4, 5, 6]
    dice_count = input("How many dice do you want to roll?\n> ")
    print_length = input("How many rolls would you like me to print?\n> ")

    try:
        print_length = int(print_length)
        dice_count = int(dice_count)
        while dice_count > dice_rolls:
            x = randint(0, 5)
            if dice_rolls < print_length:
                print(f"Dice {dice_rolls + 1} = {dice[x]}")
            dice_rolls += 1
            dice_results.append(dice[x])

    except ValueError:
        print("You have to pick a number...!")
        dice_roll()

    num = 0
    print("..............")
    while num <= 5:
        num += 1
        dice_stats = dice_results.count(num)
        if num in dice_results:
            print(f"The number {num} was rolled {dice_stats} times.  Or {(dice_stats / dice_count) * 100}% of the time.")
            while num in dice_results:
                dice_results.remove(num)
        else:
            print(f"There were no {num}'s rolled.")

    again = input("Do you want to roll again? Press 'y'\n> ")
    if again == 'y':
        dice_roll()
    else:
        print("Ok, BYE!")
        exit(0)

dice_roll()
