#http://usingpython.com/guis-and-functions/
from Tkinter import *
import random


root = Tk()

doorToGuess = random.randint(0,2)

def checkDoor(number):
    global doorToGuess

    if number == doorToGuess:
        lbl.configure(text="YES")
    else:
        lbl.configure(text="NO")

lbl = Label(root, text="Which door contains the prize?")
lbl.pack()

for i in range(3):
    btn = Button(text="Door " + str(i), command= lambda doorNo=i: checkDoor(doorNo))
    btn.pack(side=LEFT)



root.mainloop()
