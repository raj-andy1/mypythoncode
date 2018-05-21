"""
Homework 2- AnandthirthRajagopalan
"""

COST_PER_HAMBURGER = 3.00
COST_PER_HOTDOG = 2.00
COST_PER_MILKSHAKE = 3.00
TAX_RATE = 0.1

def calculateBill(numOfHB,numOfHD,numOfMS):
    totalAmtBeforeTax = numOfHB * COST_PER_HAMBURGER + numOfHD * COST_PER_HOTDOG \
                        + numOfMS * COST_PER_MILKSHAKE
    #print (totalAmtBeforeTax)
    totalAmtAfterTax = totalAmtBeforeTax + (totalAmtBeforeTax * TAX_RATE)
    #print (totalAmtAfterTax)
    return (totalAmtAfterTax)


bill1 = calculateBill (3,2,1)
print ("Here is the first bill $" + str(bill1))
bill2 = calculateBill (8,8,8)
print ("Here is the second bill $" + str(bill2))

userNuOfHB = input ("Enter the number of Hamburgers:")
userNuOfHD = input ("Enter the number of HotDogs:")
userNuOfMS = input ("Enter the number of Milk shakes:")
bill3 = calculateBill(float(userNuOfHB), float(userNuOfHD), float(userNuOfMS))
print ("Here is the final bill $" + str(bill3))
bills = bill1 + bill2 + bill3
print ("Total of all bills is $" + str(bills))
    

