"""
Homework 6 - Anandthirth Rajagopalan
SlotMachine Start.py
"""



import random
import time
import sys

reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', \
              'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries', \
              'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7']
#fixed missing ' on ln 12 col 61
#nPicturesInReel should be the length of the list and not the list itself
nPicturesInReel = len(reelList)

nCoins = 100
print( 'You have', nCoins, 'coins to start.  Good luck.')
print()

#change 'function' to 'def'
def payTable(myList):
    picture1 = myList[0]
    picture2 = myList[1]
    picture3 = myList[2]
    if myList.count(picture1) == 3:
        if picture1 == 'Lucky 7':
            nCoinsWon = 500
        elif picture1 == 'bar':
            nCoinsWon = 100
        else:
            nCoinsWon = 10
#change to picture3
    else:
        if (picture1 == picture2) or (picture2 == picture3) or (picture1 == picture3):
            nCoinsWon = 2
        else:
            nCoinsWon = 0
#missing return value
    return nCoinsWon
        

while True:
#bet should be an integer, hence convert the input str to type int
#validate number of coins and ensure it is a positive value
    bet = input('How many coins do you want to bet (defaults to 1, enter 0 to quit): ')

    if bet == 0:
        print( 'Sorry to see you go.  Come back again soon.')
        sys.exit(0)     # New, but works to quit the program
    if bet == '':
        bet = 1
    try:
        bet = int(bet)
        if bet < 0:
            print ('Sorry you have to enter a positive number')
            continue
    except:
        print ('Sorry you have not entered a valid number, please enter a valid number of coins')
        continue
    if nCoins < bet: #Validate if there are enough coins to place a bet
        print('Sorry you dont have enough coins, you only have ' + str(nCoins) + ' coins')
        continue

    resultList = []
    for spin in range(3):
        thisReelIndex = random.randrange(0, nPicturesInReel)
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print( 'Spinning ... ')
    print()
    time.sleep(.5)
    print( '     ', resultList[0])
    time.sleep(.5)
    print( '     ', resultList[1])
    time.sleep(.5)
    print( '     ', resultList[2])
    print( )
        
    nCoins = nCoins - bet
    payOut = bet * payTable(resultList)

#add an additional =

    if payOut == 0:
        print( 'Sorry - you lose.')
    else:
        print( 'You won', payOut, ' coins.  Cha-ching!')
        if payOut > 50:
            print( '                         WOOOOO  HOOOOOOOOOOO!!!!')
            
    nCoins = nCoins + payOut
#nCoins is a integer, convert it to a string
#add a space
    print( 'You now have' + ' ' + str(nCoins) + 'coins.')
    print()
    
