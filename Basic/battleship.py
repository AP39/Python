""" This program allows the player t play a 'Battleship' style game against the computer.
    The player and computer each has a 3 x 3 grid where they can place their battleship
    in one space.  The computer's battleship placement and bombings are all random.
"""
from random import randint
from random import choice
import time

print("Welcome to Python Battleship!")

player_grid = {

                'A1' : 0, 'A2' : 0, 'A3' : 0,
                'B1' : 0, 'B2' : 0, 'B3' : 0,
                'C1' : 0, 'C2' : 0, 'C3' : 0,
}

computer_grid = {

                'A1' : 0, 'A2' : 0, 'A3' : 0,
                'B1' : 0, 'B2' : 0, 'B3' : 0,
                'C1' : 0, 'C2' : 0, 'C3' : 0,
}

def start():
#asks for user input on battleship placement and has the computer automatically place theirs.
    print("Where do you want to place your battleship?  You have a 3x3 grid, A, B, C - 1, 2, 3!")
    for key in player_grid:
        player_grid[key] = 0
    player_battleship = input("> ")
    player_battleship = player_battleship.title()
    player_grid[player_battleship] = 1
    print(player_grid)

    print("The computer will now place it's battleship...")
    for key in computer_grid:
        computer_grid[key] = 0
    computer_battleship = choice(['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'])
    computer_grid[computer_battleship] = 1
    print(computer_grid)

    print("LET'S BATTLE!")
    time.sleep(1)
    battle()

def battle():
#this is where thegame takes place.  it will loop until the player or computer sinks the other's battleship
    player_bomb = input("Choose a grid square to bomb.\n> ")
    player_bomb = player_bomb.title()
    print(computer_grid)

    if computer_grid[player_bomb] == 1:
        print("\nBOOOOOOOOOOOOOOOOOOM!!!\n")
        time.sleep(2)
        print(f"YOU BOMBED {player_bomb} AND SUNK THE COMPUTER'S BATTLESHIP!!!")
        time.sleep(1)
        ending()

    else:
        print(f"You bombed {player_bomb} and missed...")
        time.sleep(1)

    print("Watch out!  The computer is bombing...")
    time.sleep(1)
    computer_bomb = choice(['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'])

    if player_grid[computer_bomb] == 1:
        print("\nBOOOOOOOOOOOOOOOOOOM!!!\n")
        time.sleep(2)
        print(f"The computer bombed {computer_bomb} and SUNK YOUR BATTLESHIP!")
        ending()

    else:
        print(f"The computer bombed {computer_bomb} and missed...")
        time.sleep(1)
        battle()

def ending():
#this allows the player to play another game after winning or losing.
    again = input("Would you like to play again?  'y' or 'n'?\n> ")

    if again == 'y':
        start()

    else:
        print("Ok, BYE!")
        exit(0)

start()
