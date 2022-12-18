import time
import random

class coin(object):
    def __init__(self):
        self.sides = ['Heads', 'Tails']
        self.side = random.choice(self.sides)
        self.history = []
    def flip(self):
        self.side = random.choice(self.sides)
        self.history.append(self.side)
    def toss(self):

        
    def getHistory(self):
        return self.history
    def __str__(self):
        return self.side

class call(object):
    def __init__(self):
        self.history=[]
        self.call=self.headsOrTails()
    def headsOrTails(self):
        try:
            userCall=str(input('Heads or Tails? Call it: ')).title()
            assert userCall=='Heads' or userCall=='Tails'
            self.history.append(userCall)
            return userCall
        except:
            print(f"'{userCall}' is not a valid call. Please enter 'Heads' "\
                  + "or 'Tails'")
            return self.headsOrTails()
    def getCall(self):
        if len(self.history) >= 1:
            return "You called " + "\"" + str(self.call) + "\""
    def getHistory(self):
        return self.history   
    def __str__(self):
        return self.call

