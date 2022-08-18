# setup
import os
import time

global days
global daysshort
global everyone
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
daysshort = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
everyone = []


def wait(t): # time lib wait function
    time.sleep(t)


def AutoLoad():
    everyone.append("trey")
    everyone.append("tttt")
    globals()["trey"] = []
    globals()["tttt"] = []

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
        print("____times tbd")


def add(inputname): # add someone new and their hours list
    if inputname in everyone:
        print("That person already exists")
        wait(t=1)
        return
    else:
        everyone.append(inputname)
        globals()[str(inputname)] = []
        return


def remove(PersonSelected): # remove a person and their hours
    everyone.pop(everyone.index(PersonSelected))
    globals()[str(PersonSelected)] = []

def edit(PersonSelected): # edit a person and their hours
    while True: # select day and hours
        print(PersonSelected) # debug printouts
        print(globals()[str(PersonSelected)]) # persons hour lists
        dayslower = []
        for i in range(len(days)):
            dayslower.append(days[i].lower())

        print(f"ADD TIMES FOR {PersonSelected}")
        for i in range(len(days)):
            print(f"{i+1} - {days[i]}")
        print("Options: (type and ENTER) \n - [DAY] | to select a day \n - cancel | to go back ")
        inputoption = input("|>  ")  # input

        if inputoption.lower == "cancel":
            return
        try:
            if int(inputoption)-1 in len(days):
                DaySelected = days[int(inputoption)-1]
                break
        except:
            if inputoption.lower() in dayslower:
                DaySelected = days[days.index(inputoption)]
                break
            else:
                print("invalid input")
                wait(t=1)
                continue
        print(DaySelected)

        print("Enter a starting time")
        inputstart = input("|>  ")  # input
        print("Enter an ending time")
        inputend = input("|>  ")  # input



        ### need to re evaluate setup of algorithm to edit hours & sleep




AutoLoad()
while True: # main loop
    os.system("cls") # clear command prompt screen
    print("ROSTER")
    PrintRoster(numbered=False,times=True) # print roster
    print("Options: (type and ENTER) \n - add [PERSON] | to add someone new \n - remove [PERSON] | to remove someone \n - edit [PERSON] | to edit someone \n (CASE SENSITIVE)") # options
    inputoption = input("|>  ") # input

    # options
    if inputoption.lower()[0:3] in "add": # if add option selected
        print(inputoption.lower()[0:3],"\n",inputoption[4:])
        add(inputname=inputoption[4:])

    if inputoption.lower()[0:6] in "remove": # if remove option selected
        print(inputoption.lower()[0:6], inputoption[7:])
        if len(everyone) < 1:
            print("There is nobody to remove")
            wait(t=1)
            continue
        elif inputoption[7:] in everyone:
            remove(PersonSelected=inputoption[7:])
            continue
        else:
            print("Invalid input")
            wait(t=1)
            continue

    if inputoption.lower()[0:4] in "edit": # if edit option selected
        print(inputoption.lower()[0:4],"\n",inputoption[5:])
        if len(everyone)<1:
            print("There is nobody to edit")
            wait(t=1)
            continue
        elif inputoption[5:] in everyone:
            edit(PersonSelected=inputoption[5:])
            continue
        else:
            print("Invalid input")
            wait(t=1)
            continue



    # debug options
    if inputoption.lower() == "dellast":
        everyone.pop(-1)
        continue
    if inputoption.lower() == "delfirst":
        everyone.pop(0)
        continue
    if inputoption.lower() == "clear":
        everyone = []
        continue


