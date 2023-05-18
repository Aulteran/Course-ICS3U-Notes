# Created on Python 3.10.11
# pip install tk

# Create a program that will ask the user to enter a number in a box. When
# they click on a button it will add that number to a total and display it in
# another box. This can be repeated as many times as they want and keep
# adding to the total. There should be another button that resets the total back
# to 0 and empties the original text box, ready for them to start again.

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Counta Van Count")
window.geometry("300x100")

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