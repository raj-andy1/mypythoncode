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
or anything else to quit')
    if userInput == 'n':
        myIndex += 1
        print (myIndex)
        while myIndex <= len(myList):
            print ('Next item in list is',myList[myIndex])
            if myIndex > len(myList):
                myIndex = (myIndex % len(myList))
            else:
                break
                
    elif userInput == 'p':
        myIndex -= 1
        print (myIndex) 
        print ('Previous item in list is',myList[myIndex])
    else:
        break
print ("Ok BYE")
        

