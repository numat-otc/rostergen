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
root.resizable(False, False)  # disable window resizing
root.geometry("1280x720")  # window size
root.configure(bg=BaseBG)  # background colour

frame1 = Frame(root);   frame1.pack(side=TOP)
frame2 = Frame(root);   frame2.pack(side=TOP)
endframe = Frame(root); endframe.pack(side=BOTTOM)


Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).pack()

#canvas.create_rectangle(0,50,1000,110,fill=FG)
#canvas.pack()

DaySpacing=0.135; DayFontSize=20; DayFG=FG; DayBG=BG; GridCenter=0.52; DayAnchor=CENTER
banner = Label(root, text=" "*1000, font=(FONT, DayFontSize, "bold"), bg=DayBG).place(relx=0.5, rely=0.2, anchor=CENTER)
Mon = Label(root, text="Monday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter-3*DaySpacing, rely=0.2, anchor=DayAnchor)
Tue = Label(root, text="Tuesday",   font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter-2*DaySpacing, rely=0.2, anchor=DayAnchor)
Wed = Label(root, text="Wednesday", font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter-DaySpacing,   rely=0.2, anchor=DayAnchor)
Thu = Label(root, text="Thursday",  font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter,              rely=0.2, anchor=DayAnchor)
Fri = Label(root, text="Friday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter+DaySpacing,   rely=0.2, anchor=DayAnchor)
Sat = Label(root, text="Saturday",  font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter+2*DaySpacing, rely=0.2, anchor=DayAnchor)
Sun = Label(root, text="Sunday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=GridCenter+3*DaySpacing, rely=0.2, anchor=DayAnchor)

#Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)


Button(endframe, text="quit", font=(FONT, 24, "bold"), fg=FG, bg="dark red", bd=0, command=quit).pack()










root.mainloop()  # end of tk


