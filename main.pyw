# Libraries
from tkinter import *  # tkinter base lib
from tkinter import messagebox, Frame  # tkinter extra libs
import ctypes  # windows command specs
import os  # windows cmd commands lib
# all print lines are for debugging purposes, they do not show up in the final code because the file type is .pyw (no prompt only tkinter)

# ui theme colours & other
# background, foreground, midground, font
BaseBG = "grey16"
BG = "grey24"
MG = "grey32"
FG = "grey90"
FONT = "Calibri"


global days
global daysshort
global Persons
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
FSstate = False
daysshort = []
for i in range(len(days)):
    daysshort.append(days[i][:3])
Persons = ["Trey", "iiii", "tttt", "ffff"]


# FOR DEBUG (splitting strings)
globals()["TreyTimes"] = ["Mon-1800-2200", "Thu-0600-1200", "Sat-0000-0400", "Sat-0800-1200", "Sat-0200-0600", "Sat-2200-0200"]
globals()["iiiiTimes"] = ["Fri-1530-2100", "Sat-1300-2100"]
globals()["ttttTimes"] = ["Wed-0600-1200", "Wed-1800-0000", "Mon-1800-2200"]
globals()["ffffTimes"] = []
for i in range(len(globals()["TreyTimes"])):
    print(globals()["TreyTimes"][i][:3], globals()["TreyTimes"][i][4:])
print("\n\n")


# tkinter and window setup
global root
root = Tk()
frame = Frame(root)
frame.pack()
root.title("Roster")  # window title
# root.resizable(False, False)  # disable window resizing
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)  # read screen size using ctypes lib
windowsize = (1600, 900)
adjustcenter = (round(screensize[0]/2-windowsize[0]/2), round(screensize[1]/2-windowsize[1]/2))  # set window size and center
root.geometry(f"{windowsize[0]}x{windowsize[1]}+{adjustcenter[0]}+{adjustcenter[1]}")  # window size and centered
root.configure(bg=BaseBG)  # background colour


def ToggleFS(FSstate):  # fullscreen toggle
    print("\ntoggle fullscreen")

    return  # fullscreening feature doesnt work so skip this (return)

    FSstate = not FSstate
    root.attributes("-fullscreen", FSstate)
    print(f"FS {FSstate}")


def LoadPeople():  # Load ui for each person
    for a in range(len(Persons)):
        print(f"\ndisplaying {Persons[a]}")  # current person in list
        if globals()[f"{Persons[a]}Times"] == []:
            print(f"{Persons[a]} has no times")
        count = 0
        lines = 0
        # for each day, split up times variables into a list
        for b in range(len(days)):
            globals()[f"{Persons[a]}Times{daysshort[b]}"] = ""
            print(f"  creating Tk:{Persons[a]}:{daysshort[b]}")
        # per the total amount of times for the current person
        for c in range(len(globals()[f"{Persons[a]}Times"])):
            for d in range(len(days)):
                if globals()[f"{Persons[a]}Times"][c][:3] == daysshort[d]:
                    if globals()[f"{Persons[a]}Times{daysshort[d]}"] == "":
                        globals()[f"{Persons[a]}Times{daysshort[d]}"] = globals()[f"{Persons[a]}Times"][c][4:]
                    else:
                        count += 1
                        if count > lines:
                            lines = count
                        globals()[f"{Persons[a]}Times{daysshort[d]}"] = str("{}\n{}".format(globals()[f"{Persons[a]}Times{daysshort[d]}"], globals()[f"{Persons[a]}Times"][c][4:]))

        for e in range(len(days)):
            print("  {}:{}".format(daysshort[e],globals()[f"{Persons[a]}Times{daysshort[e]}"]))

        # Frame
        globals()[f"Tk{Persons[a]}Frame"] = Frame(PersonsFrame, bg=BG, height=(32 + lines * 20))  # create box for the line of person ui
        globals()[f"Tk{Persons[a]}Frame"].pack(fill="x", pady=PersonsFrameSpace)
        PersonFrame = globals()[f"Tk{Persons[a]}Frame"]  # makes reading next code easier

        # Name
        globals()[f"Tk{Persons[a]}Name"] = Label(PersonFrame, font=("Consolas", 14, "bold"), text=Persons[a], fg=FG, bg=BG)
        globals()[f"Tk{Persons[a]}Name"].place(relheight=1, relx=0, x=10, rely=0.5, anchor=W)

        # Times
        for f in range(len(days)):
            globals()[f"Tk{Persons[a]}Times{daysshort[f]}"] = Label(PersonFrame, font=("Consolas", 14), text=globals()[f"{Persons[a]}Times{daysshort[f]}"], fg=FG, bg=BG)
            globals()[f"Tk{Persons[a]}Times{daysshort[f]}"].place(relheight=1, relx=GridCenter + (f - 3) * DaySpacing, x=int(GridCenter * 16), rely=0.5, anchor=CENTER)

    # New button
    global TkAddPersonFrame, TkAddPerson
    TkAddPersonFrame = Frame(PersonsFrame, bg=BaseBG, height=40)
    TkAddPersonFrame.pack(fill="x", pady=10)
    TkAddPerson = Button(TkAddPersonFrame, font=(FONT, 12), text="➕️", width=4, fg=FG, bg="forest green", activeforeground=FG, activebackground="dark green", bd=0, command=AddPersonMenu)
    TkAddPerson.place(x=30, rely=0.5, anchor=W)
    print("Completed: load") # debug msg


def ErasePeople():
    print("REDRAWING")
    for a in range(len(Persons)):
        for b in range(len(days)):
            globals()[f"Tk{Persons[a]}Times{daysshort[b]}"].destroy()
            globals()[f"Tk{Persons[a]}Name"].destroy()
            globals()[f"Tk{Persons[a]}Frame"].destroy()
    TkAddPersonFrame.destroy()
    TkAddPerson.destroy()
    print("Completed: erase")


def EditPersonMenu():
    print("\nedit box started")
    EditPopupRoot = Toplevel(root)
    EditPopupRoot.geometry("480x320")
    EditPopupRoot.title("Edit a Person")  # window title
    EditPopupRoot.configure(bg=BaseBG)  # background colour
    EditPopupRoot.resizable(False, False)  # disable window resizing
    Label(EditPopupRoot, text="Edit a Person", font=("Tahoma", 18, "bold"), fg=FG, bg=BaseBG).pack(pady=6)  # title



    def DeletePerson(SelectedPerson):  # selected delete person
        print("\neditbox: delete selected")
        def DeleteConfirmed(SelectedPerson):
            ErasePeople()
            Persons.remove(SelectedPerson)
            globals()[f"{SelectedPerson}Times"] = []
            print(f"Deleted: {SelectedPerson}")
            LoadPeople()
            EditPopupRoot.destroy()

        SelectedPerson = SelectedPerson.get()
        if SelectedPerson != SelectPersonOptions[0]:
            PersonDelete = Button(EditPopupRoot, font=(FONT, 12, "bold"), text="CONFIRM DELETE", fg=FG, bg="red4", activeforeground=FG, activebackground="maroon", bd=8, command= lambda: DeleteConfirmed(SelectedPerson))
            PersonDelete.place(relx=0.5, y=130, anchor=N)


    def EditPerson(SelectedPerson):  # selected edit time
        print("\neditbox: edit selected")
        def DeleteTimes(SelectedTimes):
            if SelectedTimes != SelectTimesOptions[0]:
                globals()[f"{SelectedPerson}Times"].remove(SelectedTimes)
                print(f"  {SelectedTimes} deleted from {SelectedPerson}")
                print("{}:{}".format(SelectedPerson, globals()[f"{SelectedPerson}Times"]))
                EditPopupRoot.destroy()

        def EditTimes():
            pass

        SelectedPerson = SelectedPerson.get()
        if SelectedPerson != SelectPersonOptions[0]:
            Label(EditPopupRoot, text=f"Edit Times for {SelectedPerson}", font=("Tahoma", 18, "bold"), fg=FG, bg=BaseBG).place(relx=0.5, y=150, anchor=CENTER)  # name

            SelectTimesOptions = ["Select a time slot"] + globals()[f"{SelectedPerson}Times"]
            SelectedTimes = StringVar(EditPopupRoot)
            SelectedTimes.set(SelectTimesOptions[0])  # default value

            TimesMenu = OptionMenu(EditPopupRoot, SelectedTimes, *SelectTimesOptions)
            TimesMenu.place(relx=0.5, y=200, anchor=CENTER)

            TimesDelete = Button(EditPopupRoot, font=(FONT, 11, "bold"), text="DELETE", fg=FG, bg="red4", activeforeground=FG, activebackground="maroon", width=14, bd=0, command=lambda: DeleteTimes(SelectedTimes))
            TimesDelete.place(relx=0.5, x=-5, y=250, anchor=E)
            TimesEdit = Button(EditPopupRoot, font=(FONT, 11, "bold"), text="EDIT", fg=FG, bg="slateblue3", activeforeground=FG, activebackground="slateblue4", width=14, bd=0, command=lambda: EditTimes(SelectedTimes))
            TimesEdit.place(relx=0.5, x=5, y=250, anchor=W)

    def AddToPerson(SelectedPerson):  # selected add a time
        if SelectedPerson != SelectPersonOptions[0]: pass


    SelectPersonOptions = ["Select Person"] + Persons
    SelectedPerson = StringVar(EditPopupRoot)
    SelectedPerson.set(SelectPersonOptions[0])  # default value

    PersonsMenu = OptionMenu(EditPopupRoot, SelectedPerson, *SelectPersonOptions)
    PersonsMenu.place(relx=0.5, y=60, anchor=CENTER)

    PersonDelete = Button(EditPopupRoot, font=(FONT, 11, "bold"), text="DELETE PERSON", fg=FG, bg="red4", activeforeground=FG, activebackground="maroon", width=14, bd=0, command=lambda: DeletePerson(SelectedPerson))
    PersonDelete.place(relx=0.5, x=-125, y=100, anchor=CENTER)
    PersonEdit = Button(EditPopupRoot, font=(FONT, 11, "bold"), text="EDIT TIMES", fg=FG, bg="slateblue3", activeforeground=FG, activebackground="slateblue4", width=14, bd=0, command=lambda: EditPerson(SelectedPerson))
    PersonEdit.place(relx=0.5, x=0, y=100, anchor=CENTER)
    PersonAdd = Button(EditPopupRoot, font=(FONT, 11, "bold"), text="ADD TIMES", fg=FG, bg="forest green", activeforeground=FG, activebackground="dark green", width=14, bd=0, command=lambda: AddToPerson(SelectedPerson))
    PersonAdd.place(relx=0.5, x=125, y=100, anchor=CENTER)


    EditPopupRoot.mainloop()


def AddPersonMenu(): # add a new person
    print("\nadd new box started")
    AddPopupRoot = Toplevel(root)
    AddPopupRoot.geometry("320x240")
    AddPopupRoot.title("Add Someone New")  # window title
    AddPopupRoot.configure(bg=BaseBG)  # background colour
    AddPopupRoot.resizable(False, False)  # disable window resizing
    Label(AddPopupRoot, text="Add A Person", font=("Tahoma", 18, "bold"), fg=FG, bg=BaseBG).pack(pady=6)  # title

    def AddConfirm():
        print(Adding)
        AddingPerson = Adding.get() # get input from entry
        if AddingPerson in Persons:
            messagebox.showinfo("Error", f"'{AddingPerson}' already exists!")
        elif AddingPerson.isascii() == False:
            messagebox.showinfo("Error", f"invalid character found in '{AddingPerson}' ")
        elif len(AddingPerson) > 24:
            messagebox.showinfo("Error", f"input is too long, maximum 24 characters")
        else:
            AddPopupRoot.destroy()
            ErasePeople()
            Persons.append(AddingPerson)
            globals()[f"{AddingPerson}Times"] = []
            print(f"Added: {AddingPerson}")
            LoadPeople()

    Adding = Entry(AddPopupRoot, font=(FONT, 14, "bold"), justify=CENTER, width=30, fg=FG, bg=MG, bd=0)
    Adding.pack(padx=10, pady=6, ipady=6)  # entry box

    ButtonFrame = Frame(AddPopupRoot, height=100, bg=BaseBG)
    ButtonFrame.pack(fill=BOTH)
    Button(ButtonFrame, text="CANCEL", font=(FONT, 16, "bold"), fg=FG, bg="red4", activeforeground=FG, activebackground="maroon", bd=0, command=AddPopupRoot.destroy).place(relx=0, x=10, y=6, anchor=NW)  # cancel
    Button(ButtonFrame, text="CONFIRM", font=(FONT, 16, "bold"), fg=FG, bg="forest green", activeforeground=FG, activebackground="dark green", bd=0, command=AddConfirm).place(relx=1, x=-10, y=6, anchor=NE)  # confirm
    AddPopupRoot.mainloop()


# frames
global PersonsFrame, PersonsFrameSpace, ScrollWidth
BaseFrame = Frame(root, height=80, bg=BaseBG)
BaseFrame.pack(side=TOP, fill=X)
DayFrame = Frame(root, height=50, bg=BG)
DayFrame.pack(side=TOP, fill=X)
PersonsFrame = Frame(root, bg=BaseBG)
PersonsFrame.pack(side=TOP, fill=BOTH, expand=True)

# spacing for first person row
PersonsFrameSpace = 4
Spacer = Frame(PersonsFrame, bg=BaseBG, width=0, height=0).pack(pady=PersonsFrameSpace / 2)

# scrollbar
ScrollWidth=16
Scroll = Scrollbar(PersonsFrame, width=ScrollWidth)
Scroll.pack(side="right")

# title
Label(BaseFrame, text="ROSTER", font=("Tahoma", 32, "bold"), fg=FG, bg=BaseBG).place(relx=0.5, rely=0.5, anchor=CENTER)

# window buttons and hotkeys(useful if in fullscreen)
Button(BaseFrame, text="❌", width=4, font=(FONT, 14), fg=FG, bg="red4", activeforeground=FG, activebackground="maroon", bd=0, command=quit).place(relx=1, rely=0, anchor=NE)
Button(BaseFrame, text="⭕", width=4, font=(FONT, 14), fg=FG, bg="blue3", activeforeground=FG, activebackground="blue4", bd=0, command=lambda: ToggleFS(FSstate)).place(relx=1, rely=0, x=-46, anchor=NE)
Editor = Button(DayFrame, font=(FONT, 14, "bold"), text="EDIT", fg=FG, bg="slateblue3", activeforeground=FG, activebackground="slateblue4", width=7, bd=0, command=EditPersonMenu).place(x=8, rely=0.5, anchor=W)

# root.bind("<F11>", lambda: ToggleFS(FSstate))  # F11 fullscreen
root.bind("<Control-w>", quit) # Ctrl+W to quit (same as other programs like Google Chrome)


# day titles
global DaySpacing, GridCenter
DayFonting = (FONT, 20, "bold")
DaySpacing = 0.12
LineOffset = -0.06
DayY = 0.5
DayFG = FG
DayBG = BG
GridCenter = 0.56
DayAnchor = CENTER
for day in range(len(days)):
    globals()[days[day]] = Label(DayFrame, text=days[day], font=DayFonting, fg=DayFG, bg=DayBG)
    globals()[days[day]].place(relx=GridCenter + ((day - 3) * DaySpacing), rely=DayY, anchor=DayAnchor)
for line in range(len(days)):
    border = Label(bg="black").place(height=windowsize[0], width=3, relx=GridCenter+(((line-3)*DaySpacing)+LineOffset), y=80, anchor=N)




LoadPeople()
# root.after(2000, packframe3())
root.mainloop()  # end of tk
