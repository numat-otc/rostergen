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
endframe = Frame(root);                        endframe.pack(side=BOTTOM)

# Title (frame1 top)
#Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).pack(side=TOP)
Label(frame1, text="ROSTER", font=(FONT, 48, "bold"), fg=FG, bg=BG).grid(column=1)

# Fullscreen mode
FSstate=False
def ToggleFullscreen(FSstate):
    root.attributes("-fullscreen", FSstate)
    FSstate = not FSstate



# Window buttons and hotkeys(useful if in fullscreen)
Button(frame1, text="✖", width=4, font=(FONT, 14), fg=FG, bg="brown4", activeforeground=FG, activebackground="maroon", bd=0, command=quit).place(relx=1, rely=0,anchor=NE)
Button(frame1, text="☐", width=4, font=(FONT, 14), fg=FG, bg="royalblue3", activeforeground=FG, activebackground="royalblue4", bd=0, command=ToggleFullscreen(FSstate=FSstate)).place(relx=1, rely=0, x=-46,anchor=NE)

root.bind("<F11>", lambda: ToggleFullscreen(FSstate=FSstate))
root.bind("<Escape>", quit)

# Day titles (frame2 mid)
DayFonting=(FONT, 20, "bold"); DaySpacing=0.135; DayY=0.5; DayFG=FG; DayBG=BG; GridCenter=0.52; DayAnchor=CENTER # Day titles customising variables
DayList=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] # list of days (can be removed or rearranged such as "Sunday" day1)
for day in range(len(DayList)):
    globals()[DayList[day]] = Label(frame2, text=DayList[day], font=DayFonting, fg=DayFG, bg=DayBG)
    globals()[DayList[day]].place(relx=GridCenter+((day-3)*DaySpacing), rely=DayY, anchor=DayAnchor)

#Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)

# Peoples (frame3 body mid)











root.mainloop()  # end of tk


