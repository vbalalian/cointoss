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
root.geometry('350x300')
Frame=tk.Frame(root)
Frame.pack(pady=10)

COIN = coin()
callHistory = []

imagesize=(150, 150)
with Image.open('/home/vinnieb/cointoss/heads.jpg', 'r') as loadH:
    loadh=loadH.resize(imagesize)
with Image.open('/home/vinnieb/cointoss/tails.jpg', 'r') as loadT:
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
YESButton=tk.Button(Frame, text='Yes', width=10, \
    height=5, command=lambda: playAgain('Yes'))
NOButton=tk.Button(Frame, text='No', width=10, \
    height=5, command=lambda: playAgain('No'))
quitButton=tk.Button(Frame, text='Quit', command=root.destroy, width=5, height=3)

def results():
    correctAnswers=0
    for i in range(len(COIN.getHistory())):
        if COIN.getHistory()[i] == callHistory[i]:
            correctAnswers+=1
    count1 = str(len(callHistory))
    text1 = 'Out of ' + count1 + ' coinflips:'
    text2 = 'You called it right ' + str(correctAnswers) + ' times.'
    Subtitle.config(text=text1)
    resultText=tk.Label(Frame, text=text2, font=('Noto Serif', 14))
    resultText.grid(row=2, column=0, columnspan=2, pady=20)
    quitButton.grid(row=3, column=0, columnspan=2)

def playButtons():
    Subtitle.config(text='Play again?')
    YESButton.grid(row=2, column=0, pady=20)
    NOButton.grid(row=2, column=1, pady=20)
def playAgain(YN):
    YESButton.grid_remove()
    NOButton.grid_remove()
    if YN=='Yes':
        open()
    else:
        results()
def callSame(yn):
    yesButton.grid_remove()
    noButton.grid_remove()
    if yn == 'Yes':
        face=callHistory[-1]
        click(face)
    elif yn == 'No':
        playButtons()
       
def click(side):
    callHistory.append(side)
    if headsButton.winfo_ismapped():
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
            Subtitle.config(text='Oof! Better luck next time!')
    root.after(3200, compareCall)
    def callAgain():
        Subtitle.config(text='Call ' + side + ' again?')
        image.grid_remove()
        yesButton.grid(row=2, column=0, pady=20)
        noButton.grid(row=2, column=1, pady=20)
    root.after(5200, callAgain)

def subtitle():
    Subtitle.config(text='Heads or Tails?')
    Subtitle.grid(row=1, column=0, columnspan=2)
def buttons():
    headsButton.grid(row=2, column=0, pady=20)
    tailsButton.grid(row=2, column=1, pady=20)
def open():
    root.after(750, subtitle)
    root.after(1250, buttons)

open()
root.mainloop()
