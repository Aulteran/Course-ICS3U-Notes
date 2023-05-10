# Create a window that will ask the user to enter a name in a text box. When
# they click on a button it will add it to the end of the list that is displayed on
# the screen. Create another button which will clear the list.

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Name Lists")
window.geometry("200x200")

names = []
names_str = ""

def refresh_list():
    global names_str
    names_str = ""
    for name in names:
        names_str += name + "\n"
    name_list["text"] = names_str

def add_name():
    global names
    name = name_entry.get()
    names.append(name)
    refresh_list()

def reset_list():
    global names
    names = []
    refresh_list()

name_entry = Entry(window)
name_entry.place(x = 0, y = 0)

name_commit = Button(window, text = "Add Name", command = add_name)
name_commit.place(x = 0, y = 20)

reset_button = Button(window, text = "Reset", command = reset_list)
reset_button.place(x = 0, y= 40)

name_list = Message(window, text = names_str)
name_list.place(x = 0, y = 60)

window.mainloop()
