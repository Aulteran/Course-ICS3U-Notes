#Challenge 6
from tkinter import *
window = Tk()
window.geometry("800x600")
window.title("Number counter")

textbox = Entry(window)
textbox.place(x=0, y= 0)
    
num = textbox.get()

if num.isdigit():
    mylist = []
    listBox = Listbox(window)
    listBox.insert(num)
    print(listBox)

else:
    def clear_box():
        textbox.delete(0, END)

def reset():
    listBox.delete(0, END)

reset_button = Button(window, command=reset, text='Reset')
reset_button.place(x=200, y=100, width=25, height=25)

window.mainloop()