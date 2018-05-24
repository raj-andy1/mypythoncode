"""
sampleprogam15 - class4
add up numbers
"""

def calculateSum(targetNu):
    total = 0
    nextNuToAddIn = 1
    while nextNuToAddIn <= targetNu:
        total = total + nextNuToAddIn
        #print("NextNuToAddIn", nextNuToAddIn)
        #print("Total = ",total)
        nextNuToAddIn = nextNuToAddIn + 1
    return total


goAgain = 'y'
while goAgain == 'y':
    targetNum = int(input("Enter a target number"))      
    print("Sum Total from 1 to",targetNum, "is", calculateSum(targetNum))
    goAgain = input("Do you want to run this again y or n?")
print ("OK Bye!!")
