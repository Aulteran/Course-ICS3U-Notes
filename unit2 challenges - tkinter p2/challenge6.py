# Save several images in the same folder as your program and call them
# 1.gif, 2.gif, 3.gif, etc. Make sure they are all .gif files. Display one in a window
# and ask the user to enter a number. It should then use that number to
# choose the correct file name and display the correct image.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("GIF Viewer")
root.geometry("500x500")

def lookup():
    entered = int(numbox.get())
    if entered > 3 or entered < 1:
        print("Please enter a number between 1 and 3")
    path = f"C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/unit2 challenges - tkinter p2/{entered}.gif"
    img = PhotoImage(file=path)
    imglabel.config(image = img)
    imglabel.image = img


inst = Label(root, text="Enter a num 1-3")
inst.place(x = 0, y = 0)

numbox = Entry(root)
numbox.place(x = 90, y = 0)

generate = Button(root, text = "Generate", command = lookup)
generate.place(x = 190, y = 0)

mainimg = PhotoImage(file = "C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/unit2 challenges - tkinter p2/main.gif")

imglabel = Label(root, image = mainimg)
imglabel.place(x=0, y = 25)

root.mainloop()
