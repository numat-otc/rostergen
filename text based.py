# setup
import os
import time

global dayslist
global daysshortlist
global everyone
dayslist = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
daysshortlist = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
everyone = []

## AutoLoad:
# ___
# ___

def wait(t): # time lib wait function
    time.sleep(t)

def AutoSave():
    pass

def PrintRoster(numbered,times): # display names and hours
    print("═" * 24)
    for i in range(len(everyone)):
        if numbered==True: # displaying numbers corresponding to persons
            print(f"{i+1}] {everyone[i]}")
        else:
            print(everyone[i])
    print("═" * 24)
    if times == True: # displaying times (TBD)
        print("times tbd")

def add(inputname): # add someone new and their hours
    while True: # new name
        if inputname.lower() in ("cancel"): # cancel
            return
        elif inputname in everyone: # if person already exists (exact characters)
            print("Person already exists")
            wait(t=1)
        else: break
    everyone.append(inputname)
    globals()[str(inputname)] = []


def remove(): # remove a person and their hours
    os.system("cls")
    while True:
        print("REMOVING")
        PrintRoster(numbered=True,times=False)
        print("Options: (Type and ENTER) \n- type a name \n- cancel")
        inputoption = input("|>  ") # input
        inputoption = int(inputoption)
        while True:
            try:
                inputoption = int(inputoption)
                if inputoption in range(len(everyone)+1):
                    everyone.pop(inputoption-1)
                    return
                else:
                    print("number out of range")
                    wait(t=1)
                    break
            except: break
        if inputoption.lower() in ("cancel"): # cancel
            return
        elif inputoption in everyone:
            everyone.remove(inputoption)
            return
        else:
            print("Invalid response. Tip: names are case-sensitive")
            wait(t=1.5)

def edit(): # edit a person and their hours
    while True:
        while True:
            os.system("cls")
            print("EDIT")
            PrintRoster(numbered=True,times=True)
            print("Options: (Type and ENTER) \n- type a name \n- cancel \n(CASE SENSITIVE)")
            inputoption = input("|>  ") # input

            try:
                inputoption = int(inputoption)-1
                if inputoption in len(everyone):
                    PersonListLocation = inputoption
                    PersonSelected = everyone[PersonListLocation]
                break
            except: pass
            if inputoption == "cancel":
                return
            elif inputoption in everyone:
                PersonListLocation = everyone.index(inputoption)
                PersonSelected = everyone[PersonListLocation]
                break
            else:
                print("Person not found")
                wait(t=1)
        while True:
            print(PersonSelected)
            print(globals()[str(inputoption)])



while True: # main loop
    os.system("cls") # clear command prompt screen
    print("ROSTER")
    PrintRoster(numbered=False,times=True) # print roster
    print("Options: (Type and ENTER) \n- a new person \n- edit \n- remove") # options
    inputoption = input("|>  ") # input

    if inputoption.lower() in ["2","+","edit","change"]: # if edit option selected
        if len(everyone)<1:
            print("You must first add a person.")
            wait(t=1)
        else:
            edit()

    if inputoption.lower() in ["3","-","remove","delete"]: # if remove option selected
        if len(everyone) < 1:
            print("There is nobody to remove")
            wait(t=1)
        else:
            remove()

    else:
        add(inputname=inputoption)
