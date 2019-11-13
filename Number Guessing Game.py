## The number guessing game by Michael Lian Gau
# This is one of the 30 days coding challenge.


from tkinter import *
import random
import time

mw = Tk()
mw.title("Guessing game")
mw.geometry("350x100")
randNum = random.randint(1, 50)

guessText = "Guess the number between 1 and 50."
tries = 10

def checkAns(event = None):
    answer = numEntry.get()
    global tries
    if (int(answer) > randNum):
        resultLbl.config(text = "Wrong! a little lower", width = 30) 
        tries -= 1
    elif(int(answer) < randNum):
        resultLbl.config(text = "Wrong! a little higher", width = 30)
        tries -= 1
    elif(int(answer) == randNum):
        resultLbl.config(text = "Congratz! You Won!", font=(None, 20), width = 30)

    if (tries == 1):
        triesLbl.config(text = "You have " + str(tries) + " try left!", font=(None, 12))
    elif(tries == 0):
        resultLbl.config(text = "You LOSE!", width = 30)
        triesLbl.config(text = "You have lost! start over?", font = (None, 12))
    elif(tries < 0):
        resultLbl.config(text = "You LOSE!", width = 30)
        triesLbl.config(text = "You have already lost! There's no point trying.", font = (None, 10))
    else:
        triesLbl.config(text = "You have " + str(tries) + " tries left!", font=(None, 12))

def reset():
    tries = 10
    randNum = random.randint(1,50)
    resultLbl.config(text = guessText, font=(None, 15), width = 30)
    triesLbl.config(text = "Starting over... You have 10 tries!", font=(None, 12))
    

resultLbl = Label(mw, text = guessText, font=(None, 15), width = 30)
resultLbl.grid(row = 0, sticky = "N")

numEntry = Entry(mw, font = (None, 15), width = 10)
numEntry.grid(row = 1, column = 0,  pady = 5)
numEntry.focus()

sendBtn = Button(mw, text = "->", width = 5, command = checkAns)
sendBtn.grid(row = 1, sticky = 'e')
mw.bind("<Return>", checkAns)

resetBtn = Button(mw, text = "Reset", width = 5, command = reset)
resetBtn.grid(row = 2, sticky = "E")

triesLbl = Label(mw, text = "You have 10 tries!", font=(None, 12))
triesLbl.grid(row = 2, sticky = "W")

mw.mainloop()

