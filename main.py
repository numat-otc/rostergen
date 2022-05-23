# Libraries
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

# Tkinter setup
root = Tk()
frame = Frame(root)
canvas = Canvas()
frame.pack()
root.title("Roster")  # window title
#root.resizable(False, False)  # disable window resizing
root.geometry("1280x720")  # window size
root.configure(bg=BaseBG)  # background colour

# Fullscreen mode
FSstate=False
def ToggleFullscreen(FSstate):
    root.attributes("-fullscreen", FSstate)
    FSstate = not FSstate


# Frames
global frame3
frame1   = Frame(root, height=80, bg=BG);                   frame1.pack(side=TOP,   fill=X)
frame2   = Frame(root, height=50, bg=BG);                   frame2.pack(side=TOP,   fill=X)
frame3   = Frame(root, height=50, width=100, bg="purple");  frame3.pack(side=TOP, fill=BOTH)
frame3Scroll = Scrollbar(frame3).pack(side="right")
#endframe = Frame(root);                        endframe.pack(side=BOTTOM)

# Title (frame1 top)
Label(frame1, text="ROSTER", font=("Tahoma", 32, "bold"), fg=FG, bg=BG).place(relx=0.5, rely=0.5, anchor=CENTER)


# Window buttons and hotkeys(useful if in fullscreen)
Button(frame1, text="✖", width=4, font=(FONT, 14), fg=FG, bg="brown4", activeforeground=FG, activebackground="maroon", bd=0, command=quit).place(relx=1, rely=0,anchor=NE)
Button(frame1, text="☐", width=4, font=(FONT, 14), fg=FG, bg="purple3", activeforeground=FG, activebackground="purple4", bd=0, command=ToggleFullscreen(FSstate=FSstate)).place(relx=1, rely=0, x=-46,anchor=NE)

#root.bind("<F11>", lambda self: ToggleFullscreen(self, FSstate=FSstate))
root.bind("<Escape>", quit)

# Day titles (frame2 mid)
DayFonting=(FONT, 20, "bold"); DaySpacing=0.135; DayY=0.5; DayFG=FG; DayBG=BG; GridCenter=0.52; DayAnchor=CENTER # Day titles customising variables
DayList=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] # list of days (can be removed or rearranged such as "Sunday" day1)
for day in range(len(DayList)):
    globals()[DayList[day]] = Label(frame2, text=DayList[day], font=DayFonting, fg=DayFG, bg=DayBG)
    globals()[DayList[day]].place(relx=GridCenter+((day-3)*DaySpacing), rely=DayY, anchor=DayAnchor)

#Open = Entry(frame2, fg=FG, bg=BG).pack(side=RIGHT)

# Peoples (frame3 body mid)
def frame3add50():
    count =+ 50
    frame3.config(height=count)

Button(frame3,text="+50px",command=frame3add50).place(relx=0.5,rely=0.5)









#root.after(2000, quit)
root.mainloop()  # end of tk


