# Challenge 4
from tkinter import *
window = Tk()
window.geometry("800x600")
window.title("Number counter")

mylist = []
def counter():
    global mylist
    mylist.append(str(textbox.get()))
    print(mylist)
    
textbox = Entry(window)
textbox.place(x=0, y= 0)
    
def reset():
    mylist=[]
    print(mylist)
    
button = Button(window, command=counter,  text="Click to add", height= 5, width=10)
button.place(x=100, y=80)

reset_button = Button(window, command=reset, text='Reset')
reset_button.place(x=200, y=100, width=25, height=25)

label=Label(window, text=mylist)
label.place(x=300, y=500, width=25, height=25)

window.mainloop()