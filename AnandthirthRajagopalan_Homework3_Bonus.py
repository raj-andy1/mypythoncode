"""
Homework 3 Bonus - Anandthirth Rajagopalan
"""

COST_OF_ADULT_TIX = 10
COST_OF_CHILD_TIX = 5

def calculateTixCost(nuOfATix,nuOfCTix,isStudent):
    totalCost = COST_OF_ADULT_TIX * nuOfATix + COST_OF_CHILD_TIX * nuOfCTix
    if isStudent:
        #print ("Student tix", isStudent)
        totalCost =  totalCost * .85
        
    return totalCost


print(calculateTixCost(10,5,False))
print(calculateTixCost(10,5,True))

adultTix = input("How many adults?")
childTix = input("How many children")
isStu = input("Are you a student? Enter Y or N")
if isStu == 'Y' or isStu == 'y':
    isStud = True
else: isStud = False

print ("Total cost of tickets is $" + str(calculateTixCost(int(adultTix), int(childTix), isStud)))
