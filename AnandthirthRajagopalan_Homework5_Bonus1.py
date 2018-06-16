"""
Homework5 - Bonus1 - Anandthirth Rajagopalan
"""

import random

myList = ['a','b','c','d','e','f','g','h','i','j','k','l']
myIndex = 0

#print ('My List is',myList)
myIndex = random.randrange(0,len(myList))
print ('Random index is',myIndex)
print ('Random list item is',myList[myIndex])
while True:
    userInput = input('Press p for previous, n for next, \
or q to quit')
    if userInput == 'n':
        myIndex += 1
        if myIndex < len(myList):
            print ('Next item in list is',myList[myIndex])
        else:
            print ('Range exceeded')
            myIndex = myIndex % len(myList)
            print ('Wrapping around, Next item in list is',myList[myIndex])
    elif userInput == 'p':
        myIndex -= 1
        if abs(myIndex) <= len(myList):
            print (myIndex)
            print ('Print previous item in list is',myList[myIndex])
        else:
            print ('Range exceeded')
            myIndex = myIndex % len(myList)
            print ('Wrapping around, Next item in list is',myList[myIndex])
    elif userInput == 'q':
        break
print ("Ok BYE")
        

