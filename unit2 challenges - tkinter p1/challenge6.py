# Create a window that will ask the user to enter a number in a text box.
# When they click on a button it will use the code variable.isdigit() to check to
# see if it is a whole number. If it is a whole number, add it to a list box,
# otherwise clear the entry box. Add another button that will clear the list.

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Hole Numba Chekca")
window.geometry("200x200")

def add_listBox(num):
    listbox.insert(END, num)

def clear_entry():
    num_entry.delete(0, END)

def verify():
    input_num = num_entry.get()
    if input_num.isdigit():
        add_listBox(input_num)
    else:
        clear_entry()

def clear_list():
    listbox.delete(0, END)

Label(window, text = "Enter a number:").place(x=0, y=0)

num_entry = Entry(window)
num_entry.place(x=0, y=25)

verify_button = Button(window, text = "Check", command = verify)
verify_button.place(x = 0, y = 45)

reset_button = Button(window, text = "Reset", command = clear_list)
reset_button.place(x = 45, y = 45)

listbox = Listbox(window)
listbox.place(x = 0, y = 65)

window.mainloop()
