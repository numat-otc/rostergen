import os

global dayslist
dayslist = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def PrintRoster():
    pass

def add():
    while True:
        os.system("cls")
        print("Type 'Cancel' to go back")
        print("═" * 24)
        print("\nType a new name and ENTER")
        inputname = input("|>  ")
        if inputname.lower() == "cancel":
            return

def remove():
    os.system("cls")
    pass

def edit():
    os.system("cls")
    pass


while True:
    os.system("cls")
    print("═" * 24)
    print("Roster:")
    PrintRoster()
    print("═" * 24)
    print("\nType 'Add' or 'Remove' or 'Edit' and ENTER")
    inputoption = input("|>  ")

    if inputoption.lower() == "add":
        add()

    if inputoption.lower() == "remove":
        remove()

    if inputoption.lower() == "edit":
        edit()

