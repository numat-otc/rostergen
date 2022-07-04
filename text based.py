import os
import time

global dayslist
global everyone
dayslist = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
everyone = []

def wait(t):
    time.sleep(t)

def PrintRoster():
    print("═" * 24)
    print("Roster:")
    for i in range(len(everyone)):
        print(everyone[i])
    print("═" * 24)

def add():
    while True:
        os.system("cls")
        PrintRoster()
        print("Type 'Cancel' to go back")
        print("\nType a new name and ENTER")
        inputname = input("|>  ")
        if inputname.lower() == "cancel":
            return
        elif inputname in everyone:
            print("Person already exists")
            wait(t=1)
            continue
        else:break

    #everyone.append(inputname)
    #return
    while True:
        print("hours entry tbd")




def remove():
    os.system("cls")
    PrintRoster()
    pass #tbd

def edit():
    os.system("cls")
    PrintRoster()
    pass #tbd


while True:
    os.system("cls")
    PrintRoster()
    print("\nType 'Add' or 'Remove' or 'Edit' and ENTER")
    inputoption = input("|>  ")

    if inputoption.lower() in ["+","add"]:
        add()

    if inputoption.lower() in ["-","remove","delete"]:
        remove()

    if inputoption.lower() in [".","edit","change"]:
        edit()


