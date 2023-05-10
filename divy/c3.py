# Challenge 3
from tkinter import *
window = Tk()
window.geometry("800x600")
window.title("Number counter")

count = 0
def counter():
    global count
    count+=int(textbox.get())
    print(count)
    label["text"] = count
    
textbox = Entry(window)
textbox.place(x=0, y=0)
    
def reset():
    global count
    count = 0
    textbox.delete(0, END)
    print(count)
    label["text"] = count
    
button = Button(window, command=counter,  text="Click to add", height= 5, width=10)
button.place(x=100, y=80)

reset_button = Button(window, command=reset, text='Reset')
reset_button.place(x=200, y=100, width=25, height=25)

label=Label(window, text=count)
label.place(x=300, y=500, width=25, height=25)

window.mainloop()