from tkinter import *  # tkinter lib
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
frame.pack()
root.title("Roster")  # window title
root.resizable(False, False)  # disable window resizing
root.geometry("1280x720")  # window size
root.configure(bg=BaseBG)  # background colour

topframe = Frame(root); topframe.pack(side=TOP)
middleframe = Frame(root); middleframe.pack(side=TOP)
bottomframe = Frame(root); bottomframe.pack(side=TOP)
endframe = Frame(root); endframe.pack(side=BOTTOM)


text = Label(topframe, text="top", font=(FONT, 48, "bold"), fg=FG, bg=BG).pack()

text = Label(middleframe, text="middle", font=(FONT, 24, "bold"), fg=FG, bg=BG).pack(side=LEFT)
Open = Entry(middleframe, fg=FG, bg=BG).pack(side=RIGHT)

text = Label(bottomframe, text="bottom", font=(FONT, 24, "bold"), fg=FG, bg=BG).pack()

text = Label(endframe, text="end", font=(FONT, 24, "bold"), fg=FG, bg=BG).pack()










root.mainloop()  # end of tk
