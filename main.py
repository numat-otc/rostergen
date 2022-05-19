from tkinter import *
from tkinter import Canvas, Frame
import random  # random lib
import os  # windows cmd commands lib
##-\‽/\TREY/\‽/-##


### UI Theme Colours
BaseBG = ("grey16",)
BG = ("grey30",)
FG = ("grey80",)
FONT = ("Calibri")
Theme=0


root = Tk()
frame = Frame(root)
canvas = Canvas()
frame.pack()
root.title("Roster")  # window title
#root.resizable(False, False)  # disable window resizing
root.geometry("1280x720")  # window size
root.configure(bg=BaseBG)  # background colour

# Frames
frame1   = Frame(root, bg=BG);                 frame1.pack(side=TOP,   fill=X)
frame2   = Frame(root, height=50, bg=BG);      frame2.pack(side=TOP,   fill=X)
frame3   = Frame(root, bg="grey20");           frame3.pack(side=RIGHT, fill=Y)
endframe = Frame(root); endframe.pack(side=BOTTOM)

# Title (frame1 top)
#Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).pack(side=TOP)
Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).grid(column=1)

# Exit button
Button(frame1, text="X", font=(FONT, 16, "bold"), fg=FG, bg="purple4", bd=0, command=quit).place(relx=1, rely=0,anchor=NE)


# Day titles (frame2 mid)
DayFonting=(FONT, 20, "bold"); DaySpacing=0.135; DayY=0.5; DayFG=FG; DayBG=BG; GridCenter=0.52; DayAnchor=CENTER # Day titles customising variables
DayList=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] # list of days (can be removed or rearranged such as "Sunday" day1)
for day in range(len(DayList)):
    globals()[DayList[day]] = Label(frame2, text=DayList[day], font=DayFonting, fg=DayFG, bg=DayBG)
    globals()[DayList[day]].place(relx=GridCenter+((day-3)*DaySpacing), rely=DayY, anchor=DayAnchor)
#Mon = Label(frame2, text="Monday",    font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter-3*DaySpacing, rely=DayY, anchor=DayAnchor)
#Tue = Label(frame2, text="Tuesday",   font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter-2*DaySpacing, rely=DayY, anchor=DayAnchor)
#Wed = Label(frame2, text="Wednesday", font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter-DaySpacing,   rely=DayY, anchor=DayAnchor)
#Thu = Label(frame2, text="Thursday",  font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter,              rely=DayY, anchor=DayAnchor)
#Fri = Label(frame2, text="Friday",    font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter+DaySpacing,   rely=DayY, anchor=DayAnchor)
#Sat = Label(frame2, text="Saturday",  font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter+2*DaySpacing, rely=DayY, anchor=DayAnchor)
#Sun = Label(frame2, text="Sunday",    font=DayFonting, fg=DayFG, bg=DayBG).place(relx=GridCenter+3*DaySpacing, rely=DayY, anchor=DayAnchor)

#Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)

# Peoples (frame3 body mid)











root.mainloop()  # end of tk


