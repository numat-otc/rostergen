from tkinter import *
from tkinter import Canvas, Frame
import random  # random lib
import os  # windows cmd commands lib

### UI Theme Colours
BaseBG = "grey16"
BG = "grey30"
FG = "grey80"
FONT = "Calibri"
##‽TREY‽NUMA‽##

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


text = Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).pack()

#canvas.create_rectangle(0,50,1000,110,fill=FG)
#canvas.pack()

DaySpacing=0.135; DayFontSize=22; DayFG=FG; DayBG="white"
banner = Label(root, text=" "*1000, font=(FONT, DayFontSize, "bold"), bg=DayBG).place(relx=0.5, rely=0.2, anchor=CENTER)
Mon = Label(root, text="Monday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5-3*DaySpacing, rely=0.2, anchor=W)
Tue = Label(root, text="Tuesday",   font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5-2*DaySpacing, rely=0.2, anchor=W)
Wed = Label(root, text="Wednesday", font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5-DaySpacing,   rely=0.2, anchor=W)
Thu = Label(root, text="Thursday",  font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5,              rely=0.2, anchor=W)
Fri = Label(root, text="Friday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5+DaySpacing,   rely=0.2, anchor=W)
Sat = Label(root, text="Saturday",  font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5+2*DaySpacing, rely=0.2, anchor=W)
Sun = Label(root, text="Sunday",    font=(FONT, DayFontSize, "bold"), fg=DayFG, bg=DayBG).place(relx=0.5+3*DaySpacing, rely=0.2, anchor=W)

#Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)


text = Label(endframe, text="end", font=(FONT, 24, "bold"), fg=FG, bg=BG).pack()










root.mainloop()  # end of tk
