'''
Author: Aadil Hussain
Python Version: 3.10.11
'''
# Create a graphical user interface in Tkinter.  This interface should have input boxes that
# allow the user to input and store information in a .CSV file. Each input should be stored
# in a separate column in excel – resembling the following.
# | NAME | # OF SALES | $ VALUE EQIV |
#
# Include a separate button that will take all the information from the .CSV file and display
# it on separate lines of the Graphical User Interface.
#
# ICS 3U EXTENSIONS:
# 1)	There must be a popup box to confirm the entry on to the CSV
# 2)	When the entry has been added successfully, have a picture to confirm
#       the success or failure of the entry. (ie. Checkmark and X symbol)

import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("SalesManager10000")
window.geometry("500x300")

FILEPATH = 'C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/SALES TEAM ASSIGNMENT/sales_db.csv'
CHECKMARK_IMG = PhotoImage(file="C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/SALES TEAM ASSIGNMENT/checkimg.png")
CROSS_IMG = PhotoImage(file="C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/SALES TEAM ASSIGNMENT/crossimage.png")

title_font = ("Arial", 12, "bold underline")

def confirmation(verified: bool):
    '''Displays image if entry added or not'''
    if verified:
        statusimg = CHECKMARK_IMG
    else:
        statusimg = CROSS_IMG
    confirmation_image_label.config(image=statusimg)
    confirmation_image_label.image = statusimg

def add_entry():
    '''Checks if num entries are valid floats,
    If not, shows popup error, If yes-> write entry'''
    name = name_entry.get()
    num_sales = num_sales_entry.get()
    value = value_entry.get()
    try:
        entry = [name, float(num_sales), round(float(value), 2)]
    except ValueError:
        confirmation(False)
        messagebox.showerror("Error", "Please enter a valid number for sales and value inputs.")
        return
    confirm = messagebox.askquestion("Confirm", f"Do you want to add this entry?\n{entry}")
    if confirm == "no":
        return confirmation(False)
    with open(FILEPATH, 'a', encoding="UTF-8") as dbopen:
        dbwriter = csv.writer(dbopen)
        dbwriter.writerow(entry)
        dbopen.close()
        confirmation(True)

def pull_entries():
    '''Takes all entries from database,
    converts to list, returns list'''
    database = []
    with open(FILEPATH, 'r', encoding="UTF-8") as dbopen:
        dbreader = csv.reader(dbopen)
        dblist = list(dbreader)
        for row in dblist:
            if row == []:
                continue
            database.append(row)
        dbopen.close()
    return database

def display_entries():
    '''Takes all entries from database,
    for each row, create label.'''
    existing_entries_label = Label(window, text="Existing Entries", font=title_font, underline=True)
    existing_entries_label.place(x=0, y=160)
    entries = pull_entries()
    y_coord = 190
    for entry in entries:
        entry_info = f"{entry[0]}: {entry[1]} Sales, ${entry[2]}"
        Label(window, text=entry_info).place(x=10, y=y_coord)
        y_coord += 20

add_entry_section_header = Label(window, text="Add Entry", font=title_font, underline=True)
add_entry_section_header.place(x=0, y=0)

name_entry_label = Label(window, text="Name:")
name_entry_label.place(x=0, y=30)
name_entry = Entry(window)
name_entry.place(x=110, y=30)

num_sales_entry_label = Label(window, text="# of Sales:")
num_sales_entry_label.place(x=0, y=60)
num_sales_entry = Entry(window)
num_sales_entry.place(x=110, y=60)

value_entry_label = Label(window, text="Total $ Value:")
value_entry_label.place(x=0, y=90)
value_entry = Entry(window)
value_entry.place(x=110, y=90)

add_entry_button = Button(window, text="Add Entry", command=add_entry)
add_entry_button.place(x=0, y=120)

view_entries_button = Button(window, text="View All Entries", command=display_entries)
view_entries_button.place(x=70, y=120)

confirmation_image_label = Label(window)
confirmation_image_label.place(x=270, y=20)

window.mainloop()
