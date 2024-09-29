from tkinter import *

root = Tk()

# crating a label widget
myLabel1 = Label(root, text="Hello Adventurer!")
myLabel2 = Label(root, text="Roll Dice")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()