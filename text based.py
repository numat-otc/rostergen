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
            print(i+1, everyone[i])
        else:
            print(everyone[i])
        if times == True: # displaying times (TBD)
            print("times tbd")
    print("═" * 24)


def add(): # add someone new and their hours
    while True: # new name
        os.system("cls")
        PrintRoster(numbered=False,times=False)
        print("Options: \n1) type a new name \n2) cancel \n(Type and ENTER)")
        inputname = input("|>  ") # input
        if inputname.lower() == "cancel": # if canceling go back
            return
        elif inputname in everyone: # if person already exists (exact characters)
            print("Person already exists")
            wait(t=1)
            continue
        else:break
    everyone.append(inputname)



def remove(): # remove a person and their hours
    os.system("cls")
    while True:
        PrintRoster(numbered=True,times=False)
        print("Options: \n1) type a name \n2) cancel \n(Type and Enter)")
        inputoption = input("|>  ") # input
        if inputoption.lower()=="cancel":
            return
        elif inputoption in everyone:
            everyone.remove(inputoption)
            return
        else:
            print("Invalid response. Tip: names are case-sensitive")
            wait(1.5)

def edit(): # edit a person and their hours
    os.system("cls")
    PrintRoster(numbered=True,times=True)

    #next task


while True: # main loop
    os.system("cls") # clear command prompt screen
    PrintRoster(numbered=False,times=True) # print roster
    print("Options: \n1) add \n2) edit \n3) remove \n(Type and ENTER)") # options
    inputoption = input("|>  ") # input

    if inputoption.lower() in ["1","+","add","new"]: # if add option selected
        add()

    if inputoption.lower() in ["2",".","edit","change"]: # if edit option selected
        if everyone<1:
            print("You must first add a person.")
            wait(t=1)
        edit()

    if inputoption.lower() in ["3","-","remove","delete"]: # if remove option selected
        remove()




