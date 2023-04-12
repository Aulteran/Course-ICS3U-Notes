import sqlite3
from tkinter import *

def add_to_list():
    newname = sname.get()
    newgrade = sgrade.get()
    cursor.execute(""" INSERT INTO Scores (name,score)
    VALUES (?,?)""", (newname,newgrade))
    db.commit()
    sname.delete(0,END)
    sgrade.delete(0,END)
    sname.focus()

def clear_list():
    sname.delete(0,END)
    sgrade.delete(0,END)
    sname.focus()


with sqlite3.connect('TestScore.db') as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Scores(
    id integer PRIMARY KEY,
    name text,
    score integer); """
)

window = Tk()
window.title ('Test Scores')
window.geometry('450x200')

label1 = Label (text = 'Enter student name: ')
label1.place(x = 30, y = 35)

sname = Entry (text = '')
sname.place(x = 150, y = 35, width = 200, height = 25)
sname.focus()

label2 = Label (text = 'Enter studen grade: ')
label2.place(x = 30, y = 80)

sgrade = Entry(text = '')
sgrade.place(x = 150, y = 80, width = 200, height = 25)
sgrade.focus()

addbtn = Button (text = 'Add', command = add_to_list)
addbtn.place(x = 150, y = 120, width = 75, height = 25)

clearbtn = Button (text = 'Clear', command = clear_list)
clearbtn.place (x = 250, y = 120, width = 75, height = 25)

window.mainloop()
db.close()