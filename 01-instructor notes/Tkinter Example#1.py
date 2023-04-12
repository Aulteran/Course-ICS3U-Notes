from tkinter import *

def click():
    name = ent_name.get()
    mess1 = str("Hello " + name)
    output['text'] = mess1
    ent_name.focus_set()

def clear():
    ent_name.delete (0,END)
    output['text'] = ''

window = Tk()
window.title("Hello User")
window.geometry("300x500")

label = Label(window, text = "Enter your name:  ")  
label.place (x = 0 , y = 150) 


ent_name = Entry (text = "")
ent_name.place (x = 0, y = 200, width = 200, height = 25)
ent_name.focus_set()

button1 = Button(text = "Click here for greeting", command = click)
button1.place(x = 50, y = 0 , width = 150, height = 25)

button2 = Button(text = 'Clear text', command = clear)
button2.place (x = 0, y = 250)

output = Message (text = "")
output.place (x = 50, y = 80, width = 200, height = 50)
output['bg'] = 'black'
output['fg'] = 'yellow'

window.mainloop()
