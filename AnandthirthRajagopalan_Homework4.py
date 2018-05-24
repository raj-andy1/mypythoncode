"""
Homework4 - Anandthirth Rajagopalan
"""
import random

def rollDice():
    value = random.randrange(1,7)
    return value

chanceNum = 0
doubleCnt = 0

while True:
    chanceNum += 1
    dice1 = rollDice()
    dice2 = rollDice()
    print ("Chance number",chanceNum)
    print ("You rolled a",dice1,"and",dice2)
    if dice1 == dice2:
        doubleCnt += 1
        doublePercent = (doubleCnt/chanceNum) * 100
        print ("Yayy!! Its a DOUBLE")
        print ("Double Count", doubleCnt)
        print ("Double percentage",doublePercent)
    goAgain = input("Do you want to keep going? Hit Enter to continue or q to quit")
    if goAgain == 'q':
        break
print("OK Bye")
    
