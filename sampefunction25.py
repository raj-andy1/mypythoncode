"""
samplefunction 24 - class 5
Roll the dice
"""

import random

def rollDice():
    thisFace = random.randrange(0,7)
    return thisFace

while True:
    nDoubles = 0
    maxRounds = int(input("How many rounds do you want to play?"))
    if maxRounds == '':
        break
    for roundNum in range(0,maxRounds):
        dice1 = rollDice()
        dice2 = rollDice()
        if dice1 == dice2:
            nDoubles += 1
    doublePercent = (nDoubles/maxRounds) * 1
    print ('After',maxRounds,'rounds, we got',nDouble,'Doubles,with a double \
percentage of', doublePercent,'%')
    
                
