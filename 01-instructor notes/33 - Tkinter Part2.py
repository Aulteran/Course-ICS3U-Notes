from tkinter import *

def clicked ():
    sel = selectName.get()
    mesg = 'Hello ' + sel
    label ['text'] = mesg
    if sel == 'Bob':
        photo = PhotoImage (file = 'bobross.gif') #photos must be in same folder
        photobox.image = photo
    elif sel == 'Sue':
        photo = PhotoImage (file = 'sue.gif')
        photobox.image = photo
    elif sel == 'Tim':
        photo = PhotoImage (file = 'tim.gif')
        photobox.image = photo
    else:
        photo = PhotoImage (file = 'marsRover.gif')
        photobox.image = photo
    photobox ['image'] = photo
    photobox.update ()



window = Tk()
window.title("Dropdown list")
window.geometry ('1024x750')
window.wm_iconbitmap ('logo.ico') #logo/pics must be in same folder
window.configure(background = 'light green')

photo = PhotoImage(file = 'marsRover.gif')
photobox = Label (window, image = photo)
photobox.image = photo                      #keep reference to Tkinter image
photobox.place (x = 0, y = 0)

but1 = Button (text = "click to display", command = clicked)
but1.place (x=100,y = 400 , height = 40)

label = Label (text = "")
label.place (x = 300, y = 00, height = 40, width = 200)

selectName = StringVar(window)
selectName.set('select menu')
namesList = OptionMenu(window,selectName, "Bob", "Sue", "Tim")
namesList.place (x=600, y = 50)



window.mainloop()
