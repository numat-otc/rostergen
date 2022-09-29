# Libraries
from tkinter import *  # tkinter base lib
from tkinter import messagebox, Frame  # tkinter extra libs
import ctypes  # windows command specs
import os  # windows cmd commands lib
# all print lines are for debugging purpose, they do not show up in the final code because the file type is .pyw (no shell only tkinter)

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
daysshort = []
for i in range(len(days)): daysshort.append(days[i][:3])
Persons = ["Trey", "tttt"]


# FOR DEBUG (splitting strings)
globals()["TreyTimes"] = ["Mon-1800-2200", "Thu-0600-1200", "Sat-0000-0400", "Sat-0800-1200", "Sat-0200-0600", "Sat-2200-0200"]
globals()["ttttTimes"] = []
for i in range(len(globals()["TreyTimes"])):
    print(globals()["TreyTimes"][i][:3], globals()["TreyTimes"][i][4:])
print("\n\n")


# Tkinter and window setup
root = Tk()
frame = Frame(root)
frame.pack()
root.title("Roster")  # window title
# root.resizable(False, False)  # disable window resizing
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)  # read screen size using ctypes lib
windowsize = (1280, 720)
adjustcenter = (round(screensize[0]/2-windowsize[0]/2), round(screensize[1]/2-windowsize[1]/2))  # set window size and center
root.geometry(f"{windowsize[0]}x{windowsize[1]}+{adjustcenter[0]}+{adjustcenter[1]}")  # window size and centered
root.configure(bg=BaseBG)  # background colour


FSstate = False
def ToggleFullscreen(FSstate):
    root.attributes("-fullscreen", FSstate)
    FSstate = not FSstate


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

        # Name                                                              justify=LEFT, anchor=W,
        globals()[f"Tk{Persons[a]}Name"] = Label(PersonFrame, font=(FONT, 14), text=Persons[a], fg=FG, bg=BG)
        globals()[f"Tk{Persons[a]}Name"].place(relheight=1, relx=0, x=30, rely=0.5, anchor=W)

        # Delete
        globals()[f"Tk{Persons[a]}Delete"] = Button(PersonFrame, font=(FONT, 10), text="❌", width=3, fg=FG, bg="red4", activeforeground=FG, activebackground="maroon", bd=0)
        globals()[f"Tk{Persons[a]}Delete"].place(relheight=1, relx=0, rely=0.5, anchor=W)

        # Times
        for f in range(len(days)):
            globals()[f"Tk{Persons[a]}Times{daysshort[f]}"] = Label(PersonFrame, font=(FONT, 13, "bold"), text=globals()[f"{Persons[a]}Times{daysshort[f]}"], fg=FG, bg=BG)
            globals()[f"Tk{Persons[a]}Times{daysshort[f]}"].place(relheight=1, relx=GridCenter + (f - 3) * DaySpacing, x=int(GridCenter * 16), rely=0.5, anchor=CENTER)

    # New
    global TkAddPersonFrame, TkAddPerson
    TkAddPersonFrame = Frame(PersonsFrame, bg=BaseBG, height=40)
    TkAddPersonFrame.pack(fill="x", pady=10)
    TkAddPerson = Button(TkAddPersonFrame, font=(FONT, 12), text="➕️", width=4, fg=FG, bg="forest green", activeforeground=FG, activebackground="dark green", bd=0, command=AddPerson)
    TkAddPerson.place(x=30, rely=0.5, anchor=W)


def Redraw(c):
    print("REDRAWING")
    for a in range(len(Persons)+c):
        for b in range(len(days)):
            globals()[f"Tk{Persons[a]}Times{daysshort[b]}"].destroy()
        globals()[f"Tk{Persons[a]}Delete"].destroy()
        globals()[f"Tk{Persons[a]}Name"].destroy()
        globals()[f"Tk{Persons[a]}Frame"].destroy()
    TkAddPersonFrame.destroy()
    TkAddPerson.destroy()
    print("Completed redraw, calling load")
    LoadPeople()


def EditPerson():
    print("\nedit box started")
    def ConfirmEdit():
        pass

    def SelectPersonEdit():
        pass


    EditPopupRoot = Toplevel(root)
    EditPopupRoot.geometry(f"320x320")
    EditPopupRoot.title("Edit")  # window title
    EditPopupRoot.configure(bg=BaseBG)  # background colour
    EditPopupRoot.resizable(False, False)  # disable window resizing

    Label(EditPopupRoot, text="Edit", font=("Tahoma", 18, "bold"), fg=FG, bg=BaseBG).pack(pady=6)  # title

    Options = ["SELECT PERSON"] + Persons
    variable = StringVar(EditPopupRoot)
    variable.set(Options[0])  # default value
    PersonsMenu = OptionMenu(EditPopupRoot, variable, *Options)
    PersonsMenu.pack()

    EditPopupRoot.mainloop()


def AddPerson(): # add a new person
    print("\nadd new box started")
    def AddConfirm():
        adding = addentry.get() # get input from entry
        if adding in Persons:
            messagebox.showinfo("Error", f"'{adding}' already exists!")
        elif adding.isascii() == False:
            messagebox.showinfo("Error", f"invalid character found in '{adding}' ")
        elif len(adding) > 24:
            messagebox.showinfo("Error", f"input is too long, maximum 24 characters")
        else:
            AddPopupRoot.destroy()
            Persons.append(adding)
            globals()[f"{adding}Times"] = []
            print(f"Added: {adding}")
            Redraw(c=-1)


    AddPopupRoot = Toplevel(root)
    AddPopupRoot.geometry(f"320x240")
    AddPopupRoot.title("Add Someone New")  # window title
    AddPopupRoot.configure(bg=BaseBG)  # background colour
    AddPopupRoot.resizable(False, False)  # disable window resizing

    Label(AddPopupRoot, text="Add A Person", font=("Tahoma", 18, "bold"), fg=FG, bg=BaseBG).pack(pady=6)  # title
    addentry = Entry(AddPopupRoot, font=(FONT, 14, "bold"), justify=CENTER, width=30, fg=FG, bg=MG)
    addentry.pack(padx=10, pady=6, ipady=6)  # entry box
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
Button(BaseFrame, text="⭕", width=4, font=(FONT, 14), fg=FG, bg="blue3", activeforeground=FG, activebackground="blue4", bd=0, command=ToggleFullscreen(FSstate=FSstate)).place(relx=1, rely=0, x=-46, anchor=NE)
# root.bind("<F11>", lambda: ToggleFullscreen(self, FSstate=FSstate))
root.bind("<Control-w>", quit) # Ctrl+W to quit (same as other programs like Google Chrome)
Editor = Button(DayFrame, font=(FONT, 20, "bold"), text="EDIT", fg=FG, bg="slateblue3", activeforeground=FG, activebackground="slateblue4", width=7, bd=5, command=EditPerson)
Editor.place(relheight=1, x=30, rely=0.5, anchor=W)

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
