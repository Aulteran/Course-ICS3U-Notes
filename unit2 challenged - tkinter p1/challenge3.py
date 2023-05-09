# Created on Python 3.10.11
# pip install tk

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Counta Van Count")
window.geometry("400x400")

count = 0

def countup():
    global count
    count+=int(useradd.get())
    print(count)
    activecount['text'] = count

def resetcount():
    global count
    count = 0
    print(count)
    activecount['text'] = count

activecount = Label(window, text=count)
activecount.place(x=0, y=0)

useradd = Entry(window)
useradd.place(x=0, y=20)

addconfirm = Button(window, command = countup, text = "Add")
addconfirm.place(x=0, y=50)

resetbutton = Button(window, command = resetcount, text = "Reset")
resetbutton.place(x=40, y=50)

window.mainloop()