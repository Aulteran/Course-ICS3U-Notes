# Create a new program that will generate two random whole numbers
# between 10 and 50. It should ask the user to add the numbers together and
# type in the answer. If they get the question correct, display a suitable image
# such as a tick; if they get the answer wrong, display another suitable image
# such as a cross. They should click on a Next button to get another question

import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Adding Game")
root.geometry("500x500")

def ques_gen():
    rand1 = random.randint(10,50)
    rand2 = random.randint(10,50)
    return (f"{rand1} + {rand2} = ?", rand1+rand2)

def summon_ques():
    global answer
    raw_ques = ques_gen()
    questiontxt = raw_ques[0]
    answer = raw_ques[1]
    return questiontxt

def submit():
    global answer
    submitted = int(answerbox.get())
    if submitted == answer:
        print("correct")
        newimg = PhotoImage(file = 'C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/unit2 challenges - tkinter p2/checkimg.png')
    else:
        print("wrong")
        newimg = PhotoImage(file = 'C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/unit2 challenges - tkinter p2/crossimage.png')
    statusdisplay.config(image = newimg)
    statusdisplay.image = newimg

def next_q():
    question["text"] = summon_ques()

question = Label(root, text=summon_ques())
question.place(x = 0, y = 0)

answerbox = Entry(root)
answerbox.place(x = 0, y = 20)

submit_but = Button(root, text="Submit", command = submit)
submit_but.place(x = 100, y = 20)

nextbut = Button(root, text="Next Question", command = next_q)
nextbut.place(x = 150, y = 20)

statusimg = PhotoImage(file = 'C:/Users/aulte/OneDrive/Documents/GitHub/Course-ICS3U-Notes/unit2 challenges - tkinter p2/q-mark-image.png')
statusdisplay = Label(root, image = statusimg)
statusdisplay.place(x = 0, y = 45)

root.mainloop()
