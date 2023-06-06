from tkinter import *
from tkinter import ttk
from tkinter import messageBox

woot = Tk()
woot.geometry("700x200")

def on_lick():
    messageBox.showinfo("POV: bozo sees warning", "the action the bozo tryna do cannot be the opposite of done")

butt1 = Button(window, text = "open za poopup", command = on_lick)
butt1.place(x = 300, y = 0) #l bozo, 0 y axis


woot.mainloop()
