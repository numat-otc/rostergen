# setup
import os
import time

global dayslist
global daysshortlist
global everyone
dayslist = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
daysshortlist = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
everyone = []


def wait(t): # time lib wait function
    time.sleep(t)


def PrintRoster(): # display names and hours
    print("═" * 24)
    print("Roster:")
    for i in range(len(everyone)):
        print(everyone[i])
    print("═" * 24)


def add(): # add someone new and their hours
    while True: # new name
        os.system("cls")
        PrintRoster()
        print("Type 'Cancel' and ENTER to go back")
        print("Type a new name and ENTER")
        inputname = input("|>  ") # input
        if inputname.lower() == "cancel": # if canceling go back
            return
        elif inputname in everyone: # if person already exists (exact characters)
            print("Person already exists")
            wait(t=1)
            continue
        else:break
    everyone.append(inputname)
    globals()[f"list{everyone[-1]}"] = []
    while True: # new name hours
        os.system("cls")
        print("Type 'Cancel' and ENTER to go back")
        print("Type a number corresponding to a day and ENTER")
        print("Type nothing and ENTER to finish")
        print("═" * 24)
        print(f"{inputname}:")
        for i in range(len(dayslist)):
            if len(dayslist[i])<9: # align days up
                dayalign = str(" "*(9-len(dayslist[i])))
            else: dayalign = ""
            print(f"{i+1} - {dayalign}{dayslist[i]}:  ")
            # and hours

        print("═" * 24)
        inputday = input("|>  ") # input
        if inputday.lower() == "cancel": # if canceling go back
            everyone.pop(-1) # delete name from list
            return
        if inputday == "":
            pass ### save vars, go back
        print(globals()[f"list{inputname}"])
        input()



def remove(): # remove a person and their hours
    os.system("cls")
    PrintRoster()
    pass #tbd

def edit(): # edit a person and their hours
    os.system("cls")
    PrintRoster()
    pass #tbd


while True: # main loop
    os.system("cls") # clear command prompt screen
    PrintRoster() # print roster
    print("Type 1-'Add' or 2-'Remove' or 3-'Edit' and ENTER") # options
    inputoption = input("|>  ") # input

    if inputoption.lower() in ["1","+","add","new"]: # if add option selected
        add()

    if inputoption.lower() in ["2","-","remove","delete"]: # if remove option selected
        remove()

    if inputoption.lower() in ["3",".","edit","change"]: # if edit option selected
        edit()


