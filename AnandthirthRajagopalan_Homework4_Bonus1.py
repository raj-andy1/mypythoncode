"""
Homework4 - Bonus1 - Anandthirth Rajagopalan
"""

import random

def rollDice():
    value = random.randrange(1,7)
    return value

while True:
    chanceNum = 0
    doubleCnt = 0
    userCnt = int(input("How many rounds do you want to play?"))
    while chanceNum < userCnt:
        chanceNum += 1
        dice1 = rollDice()
        dice2 = rollDice()
        #print ("Dice1", dice1)
        #print ("Dice2", dice2)
        #print ("###Round",chanceNum,"###")
        if dice1 == dice2:
            doubleCnt += 1
            #print ("Double Count",doubleCnt)
    doublePercent = (doubleCnt/chanceNum) * 100
    print ("After",chanceNum,"rounds, we got",doubleCnt,"doubles with a double percentage of",doublePercent)
    goAgain = input("Do you want to keep going? Hit Enter to continue or q to quit")
    if goAgain == 'q':
        break
print("OK Bye")

    

