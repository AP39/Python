""" This script allow the user to rename files in a specific folder to a
    new name plus a sequential number.  This can be used on large folders
    of pictures, etc.  The user must input the path of the folder and the
    desired new name of the files.  The script transfers over the current
    file extensions of all files and does NOT change the name of any
    folders or files with no extension in the target folder.
"""
import os
import os.path

print("\nWELCOME TO PyRENAMER.\n\nThis will allow you to mass rename a folder's contents and will keep their current file extension (ex .jpg, .mov)\nThis script will also add sequential numbers to each file name.\n")
#this function takes the input path and desired name.  then changes the name and adds sequential numbers the the end of the fie name.
def renamer():

    i = 1
    x = 0
    path = input("Please enter or paste the path of the folder with the contents you would like to rename, ex 'C:/Users/...'\n> ")
    new_name = input("Files will be renamed with your input plus a sequential number, ex. 'Python1', 'Python2'\nWhat do you want to name these new files?\n> ")

    for filename in os.listdir(path):
        main, extension = os.path.splitext(filename)

        if len(extension) > 0:
            old = path + filename
            new = path + new_name + str(i) + extension
            os.rename(old, new)
            i += 1
#this allows any folders of other non extension files to be skipped.
        else:
            x += 1
#return statistics on the process
    print(f"RENAMING COMPLETE!\n\t{i - 1} files renamed, {x} files skipped.\n")
    repeater()
#allows the user to complete the process again on the same or different folder.
def repeater():
    again = input("Do you want to rename another folder's contents?\n'y' to continue, 'n' to quit\n> ")

    if again == 'y':
        renamer()
    else:
        print("Ok, BYE!")
        exit(0)

renamer()
