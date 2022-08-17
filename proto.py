# setup
import os
import time

global days
global daysshort
global everyone
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
daysshort = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
everyone = ["trey", "tttt"] # temporarily preset

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
        print("____times tbd")

def add(inputname): # add someone new and their hours list
    while True: # new name
        if inputname.lower() in ("cancel"): # cancel
            return
        elif inputname in everyone: # if person already exists (exact characters)
            print("Person already exists")
            wait(t=1)
            return
        else: break
    everyone.append(inputname)
    globals()[str(inputname)] = []


def remove(): # remove a person and their hours
    os.system("cls")
    while True:
        print("REMOVING")
        PrintRoster(numbered=True,times=False)
        print("Options: (Type and ENTER) \n - type a name \n - cancel")
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
    def selectday():
        while True: # select day and hours
            print(PersonSelected) # debug printouts
            print(globals()[str(inputoption)])
            dayslower = []
            for i in range(len(days)):
                dayslower.append(days[i].lower())

            for i in len(days):
                print(f"{i} - {days[i]}")
            print("Options: (Type and ENTER) \n - select a day \n - back \n - cancel \n")
            inputoption = input("|>  ")  # input

            try:
                if int(inputoption)-1 in len(days):
                    DaySelected = days[i]
                    break
            except:
                if inputoption.lower == "cancel":
                    return
                elif inputoption.lower == "back":
                    break

                elif inputoption.lower() in dayslower:
                    DaySelected = days[days.index(inputoption)]
                    break


                else:
                    print("invalid input")
                    wait(t=1)
                    continue

    def selectperson():
        global PersonSelected
        while True: # select person
            os.system("cls")
            print("EDIT")
            PrintRoster(numbered=True,times=True)
            print("Options: (Type and ENTER) \n - a name \n - cancel \n (CASE SENSITIVE)")
            inputoption = input("|>  ") # input

            try:
                if int(inputoption)-1 in len(everyone):
                    print("innn")
                    PersonListLocation = inputoption
                    PersonSelected = everyone[PersonListLocation]
                    break
            except:
                if inputoption == "cancel":
                    return
                elif inputoption in everyone:
                    PersonListLocation = everyone.index(inputoption)
                    PersonSelected = everyone[PersonListLocation]
                    break
                else:
                    print("Person not found")
                    wait(t=1)
        selectday()

    def selecthours():
        pass

    while True:
        selectperson()


        ### need to re evaluate setup of algorithm to edit hours & sleep







while True: # main loop
    os.system("cls") # clear command prompt screen
    print("ROSTER")
    PrintRoster(numbered=False,times=True) # print roster
    print("Options: (Type and ENTER) \n - [PERSON] | to add someone new \n - edit [PERSON] | to edit someone\n - remove [PERSON] | to remove someone") # options
    inputoption = input("|>  ") # input

    # options
    if inputoption.lower()[0:3] in "edit": # if edit option selected
        selectedperson = inputoption.lower()[5:-1]
        print(selectedperson)
        if len(everyone)<1:
            print("There is nobody to edit")
            wait(t=1)
            continue
        else:
            edit()
            continue
    if inputoption.lower()[0:5] in "remove": # if remove option selected
        if len(everyone) < 1:
            print("There is nobody to remove")
            wait(t=1)
            continue
        else:
            remove()
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

    add(inputname=inputoption)
