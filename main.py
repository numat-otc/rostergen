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

frame1 = Frame(root,height=50,width=10000);   frame1.pack(side=TOP)
frame2 = Frame(root,height=50,width=10000, bg=BG);   frame2.pack(side=TOP)
endframe = Frame(root); endframe.pack(side=BOTTOM)


Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).pack()

#canvas.create_rectangle(0,50,1000,110,fill=FG)
#canvas.pack()

DaySpacing=0.135; DayY=0.5; DayFontSize=20; DayFG=FG; DayBG=BG; GridCenter=0.52; DayAnchor=CENTER
Mon = Label(frame2, text="Monday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter-3*DaySpacing, rely=DayY, anchor=DayAnchor)
Tue = Label(frame2, text="Tuesday",   font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter-2*DaySpacing, rely=DayY, anchor=DayAnchor)
Wed = Label(frame2, text="Wednesday", font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter-DaySpacing,   rely=DayY, anchor=DayAnchor)
Thu = Label(frame2, text="Thursday",  font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter,              rely=DayY, anchor=DayAnchor)
Fri = Label(frame2, text="Friday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter+DaySpacing,   rely=DayY, anchor=DayAnchor)
Sat = Label(frame2, text="Saturday",  font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter+2*DaySpacing, rely=DayY, anchor=DayAnchor)
Sun = Label(frame2, text="Sunday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter+3*DaySpacing, rely=DayY, anchor=DayAnchor)

#Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)


Button(endframe, text="quit", font=(FONT, 24, "bold"), fg=FG, bg="dark red", bd=0, command=quit).pack()










root.mainloop()  # end of tk


