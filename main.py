# Libraries
from tkinter import *
from tkinter import messagebox, Frame
import ctypes
import time
import random  # random lib
import os  # windows cmd commands lib


# UI theme colours & other
BaseBG = ("grey16",)
BG = ("grey30",)
FG = ("grey80",)
FONT = ("Calibri")
Theme = 0
personlist = ['trey', 'JAY']

# Tkinter setup
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

# Fullscreen mode
FSstate = False


def ToggleFullscreen(FSstate):
    root.attributes("-fullscreen", FSstate)
    FSstate = not FSstate


# Frames
global frame3
frame1 = Frame(root, height=80, bg=BG)
frame1.pack(side=TOP, fill=X)
frame2 = Frame(root, height=50, bg=BG)
frame2.pack(side=TOP, fill=X)
frame3 = Frame(root, bg="tomato4")
frame3.pack(side=TOP, fill=BOTH, expand=True)  # change colours l8r
frame3Scroll = Scrollbar(frame3).pack(side="right")
# endframe = Frame(root)
# endframe.pack(side=BOTTOM)

# Title (frame1 top)
Label(frame1, text="ROSTER", font=("Tahoma", 32, "bold"), fg=FG, bg=BG).place(relx=0.5, rely=0.5, anchor=CENTER)
# Window buttons and hotkeys(useful if in fullscreen)
Button(frame1, text="✖", width=4, font=(FONT, 14), fg=FG, bg="brown4",  activeforeground=FG, activebackground="maroon",  bd=0, command=quit).place(relx=1, rely=0, anchor=NE)
Button(frame1, text="☐", width=4, font=(FONT, 14), fg=FG, bg="purple3", activeforeground=FG, activebackground="purple4", bd=0, command=ToggleFullscreen(FSstate=FSstate)).place(relx=1, rely=0, x=-46, anchor=NE)
# root.bind("<F11>", lambda self: ToggleFullscreen(self, FSstate=FSstate))
root.bind("<Escape>", quit)


# Day titles (frame2 mid)
# Day titles customising variables (gives me ability to easily change the style of this particular area
DayFonting = (FONT, 22, "bold")
DaySpacing = 0.12
LineOffset = -0.06
DayY = 0.5
DayFG = FG
DayBG = BG
GridCenter = 0.56
DayAnchor = CENTER
DayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # list of days (can be removed or rearranged such as "Sunday" day1)
for day in range(len(DayList)):
    globals()[DayList[day]] = Label(frame2, text=DayList[day], font=DayFonting, fg=DayFG, bg=DayBG)
    globals()[DayList[day]].place(relx=GridCenter+((day-3)*DaySpacing), rely=DayY, anchor=DayAnchor)
for line in range(len(DayList)):
    border = Label(bg="black").place(height=9000, width=3, relx=GridCenter+(((line-3)*DaySpacing)+LineOffset), y=80, anchor=N)

# Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)


# Peoples (frame3 body mid)
def addp():
    def addconfirm():
        adding = addentry.get()
        if adding.upper() in personlist:
            messagebox.showinfo("Error", f"'{adding.upper()}' already exists!")
            return
        addppopup.destroy()
        return

    addppopup = Toplevel(root)
    addppopup.title("Add Someone")  # window title
    addppopup.configure(bg=BaseBG)  # background colour
    addppopup.resizable(False, False)  # disable window resizing
    Label(addppopup, text="ADD SOMEONE NEW", font=("Tahoma", 16, "bold"), fg=FG, bg=BaseBG).grid(pady=10)  # title
    addentry = Entry(addppopup, font=(FONT, 16, "bold"), width=24, fg=FG, bg=BaseBG)
    addentry.grid(pady=10)  # entry box
    Button(addppopup, text="CANCEL", font=(FONT, 14), fg=FG, bg="brown4",  activeforeground=FG, activebackground="maroon",  bd=0, command=addppopup.destroy).grid(row=3, sticky=W)  # cancel
    Button(addppopup, text="CONFIRM", font=(FONT, 14), fg=FG, bg="green3", activeforeground=FG, activebackground="darkgreen", bd=0, command=addconfirm).grid(row=3, sticky=E)  # confirm

    addppopup.mainloop()
    addppopup.destroy()
# pack widgets


def packframe3():
    frame3contents = []
    # while True:
        # try:
    for i in range(len(frame3contents)):
        print("destroying-", globals()[str(frame3contents[i])])
        globals()[str(frame3contents[i])].destroy()
        # except:
            # pass

    for i in range(3):
        globals()["frame3.", i+1] = Frame(frame3, bg="wheat3")
        globals()["frame3.", i+1].pack(fill="x", pady=12)
        frame3contents.append("frame3"+str(i+1))

        globals()["person", i+1] = Label((globals()["frame3.", i+1]), text="abcd")
        globals()["person", i+1].grid(column=2, row=0)
        globals()["deleteperson", i+1] = Button((globals()["frame3.", i+1]), text="✖", width=4, font=(FONT, 14), fg=FG, bg="brown4", activeforeground=FG, activebackground="maroon", bd=0)
        globals()["deleteperson", i+1].grid(column=1, row=0)

        frame3contents.append("person"+str(i+1))
        frame3contents.append("deleteperson"+str(i+1))
    globals()["frame3.", i+1] = Frame(frame3, bg="wheat3")
    globals()["frame3.", i+1].pack(fill="x", pady=12)
    frame3contents.append("frame3"+str(i+1))

    addperson = Button((globals()["frame3.", i+1]), text="+", width=3, font=(FONT, 14), fg=FG, bg="green3", activeforeground=FG, activebackground="darkgreen", bd=0, command=addp).grid(padx=20)
    frame3contents.append("addperson")
    print(frame3contents)


packframe3()
# root.after(2000, packframe3())
root.mainloop()  # end of tk
