#### Tkinter EXAMPLES EXPLAINED  ####

from tkinter import *

#key down function
def click():
    entered_text = text_entry.get() #this will collect entry from entry box
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "sorry there is no word try again"
    output.insert (END, definition)

#exit function
def done():
    window.destroy()
    exit()


window = Tk()
window.title("My Comp Science Glossary")
window.geometry("800x600")
window.configure(background = 'black')



#create label
Label (window, text = "Enter the word you like a definition for:",
       bg = 'black', fg = 'white', font = 'none 12 bold').grid(row=1,column = 0, sticky = W)

#create a text entry box

text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=2, column = 0, sticky = W)

#add a submit button
Button(window, text = "SUBMIT", width = 6, command = click).grid(row=3, column =0, sticky = W)

#create another label
Label (window, text = "\nDefinition", bg = 'black', fg='white', font = 'none 12 bold').grid(row =4, column = 0, sticky = W)

#create an output box
output = Text (window, width = 75, height = 6, wrap = WORD, background = 'white')
output.grid (row=5, column = 0, columnspan = 2, sticky = W)

#dictionary
my_compdictionary = {
    "algorithm": "step by step instructions",
    'bug':'a piece of code that does not work'}

#Exit Label
Label (window, text = "click to Exit:",
       bg = 'black', fg = 'white', font = 'none 12 bold').grid(row=6,column = 0, sticky = W)

#Exit Button
Button(window, text = "EXIT", width = 14, command = done).grid(row=7, column =0, sticky = W)

window.mainloop()
