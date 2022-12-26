import random
import tkinter as tk
from PIL import Image, ImageTk

class coin(object):
    def __init__(self):
        self.sides = ['Heads', 'Tails']
        self.side = random.choice(self.sides)
        self.history = []
    def flip(self):
        self.side = random.choice(self.sides)
        self.history.append(self.side)
    def getHistory(self):
        return self.history
    def __str__(self):
        return self.side
root = tk.Tk()
root.geometry('350x290')
Frame=tk.Frame(root)
Frame.pack()

COIN = coin()
coinHistory, callHistory = [], []

imagesize=(150, 150)
with Image.open('/home/vinnieb/cointoss/heads.jpg', 'r')\
    as loadH:
    loadh=loadH.resize(imagesize)
with Image.open('/home/vinnieb/cointoss/tails.jpg', 'r')\
    as loadT:
    loadt=loadT.resize(imagesize)
heads=ImageTk.PhotoImage(loadh)
tails=ImageTk.PhotoImage(loadt)
image = tk.Label(Frame)

Title=tk.Label(Frame, text='Welcome to Cointoss!', \
                font=('Noto Serif',16,'bold'))
Title.grid(row=0, column=0, columnspan=2, pady=15)
Subtitle=tk.Label(Frame, font=('Noto Serif', 14))
headsButton=tk.Button(Frame, text='Heads', width=10, \
    height=5, command=lambda: click('Heads'))
tailsButton=tk.Button(Frame, text='Tails', width=10, \
    height=5, command=lambda: click('Tails'))
yesButton=tk.Button(Frame, text='Yes', width=10, \
    height=5, command=lambda: callSame('Yes'))
noButton=tk.Button(Frame, text='No', width=10, \
    height=5, command=lambda: callSame('No'))

def callSame(yn):
    yesButton.grid_remove()
    noButton.grid_remove()
    if yn == 'Yes':
       ### WHERE I LEFT OFF: if yes, find a way to call again(might have to rework functions)
    elif yn == 'No':
       ## restore call (maybe just move specific functions back outside current nested spots)
def click(side):
    callHistory.append(side)
    headsButton.grid_remove()
    tailsButton.grid_remove()
    Subtitle.config(text='You called '+ side)
    def flipText():
        Subtitle.config(text='Flipping the coin...')
    root.after(900, flipText)
    def coinFlip():
        COIN.flip()
        Subtitle.config(text='The coin shows ' + \
            str(COIN))
        if str(COIN) == 'Heads':
            image.config(image=heads)
            image.grid(row=2, column=0, columnspan=2, pady=10)
        elif str(COIN) == 'Tails':
            image.config(image=tails)
            image.grid(row=2, column=0, columnspan=2, pady=10)
    root.after(1800, coinFlip)
    def compareCall():
        if str(side) == str(COIN):
            Subtitle.config(text='Good job! You called it!')
        else:
            Subtitle.config(text='Oof! Better luck next time...')
    root.after(3200, compareCall)
    def callAgain():
        Subtitle.config(text='Call ' + side + ' again?')
        image.grid_remove()
        yesButton.grid(row=2, column=0, pady=20)
        noButton.grid(row=2, column=1, pady=20)
    root.after(4700, callAgain)

def open():
    def subtitle():
        Subtitle.config(text='Heads or Tails?')
        Subtitle.grid(row=1, column=0, columnspan=2)
    def buttons():
        headsButton.grid(row=2, column=0, pady=20)
        tailsButton.grid(row=2, column=1, pady=20)
    root.after(750, subtitle)
    root.after(1250, buttons)

#8 compare user's call to result
#9 play same call?
#10 if so, start over
        #11 if not, ask for new call, give choice to quit
#12 if user quits, display session history

open()
root.mainloop()
