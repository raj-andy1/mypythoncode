"""
sampleFunction2 py file
"""

def addTwo(startingValue):
    endingValue = startingValue + 2
    print ("The sum of", startingValue, "and 2 is:",endingValue)

addTwo(4)
addTwo(223)
addTwo(-25)
addTwo(55.37)

userNumber = input("Enter a number:")
#userNumber = int(userNumber)
addTwo(int(userNumber))
