"""This script creates a random password of 3 possible lengths.  All passwords may contain letters, numbers
    or special characters.  After creation the choice is given to copy the new password to the clipboard.
"""


def passgen():
    import random
    import string
    import pyperclip

    print("\n\n******** Welcome to PasswordGen ********\n\nThis program will generate a random password tailored to your needs.")
    print("About how long would you like your password?")
    print("For 8 -> 10 characters, press 1")
    print("For 11 -> 15 characters, press 2")
    print("For 16 -> 25 characters, press 3")
    choice = int(input(">  "))

    if choice == 1:
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(random.randint(8, 11))])

    elif choice == 2:
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(random.randint(11, 16))])

    elif choice == 3:
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(random.randint(16, 26))])

    else:
        passgen()


    print("You new password is --->    ", password)
    clipboard = input("Would you like to copy password to clipboard? Press 'y' or any key to cancel\n>  ")
    if clipboard == 'y':
        pyperclip.copy(password)
        print("Ok, Copied!")

    again = input("\n\nWould you like to make another password? Press 'y' or any key to quit\n>  ")

    if again == 'y':
        passgen()

    else:
        exit(0)


passgen()
