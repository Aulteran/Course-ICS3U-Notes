'''
Author: Aadil Hussain
Python Version: 3.10.4
'''

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("times tables go brrrr")
window.geometry("500x500")

def gen_times_table():
    num = int(enternum_box.get())
    for i in range(1,13):
        item = f"{i} x {num} = {i*num}"
        times_tables.insert(END, item)

def clearbox():
    times_tables.delete(0, END)

enternum_label = Label(window, text="Enter a number:")
enternum_label.place(x=0, y=0)

enternum_box = Entry(window)
enternum_box.place(x=120,y=0)

times_tables = Listbox(window)
times_tables.place(x=120, y=20)

viewbutton = Button(window, text="View Times Table", command=gen_times_table)
viewbutton.place(x=250, y=0)

clearbutton = Button(window, text="Clear", command=clearbox)
clearbutton.place(x=250, y=30)

window.mainloop()
