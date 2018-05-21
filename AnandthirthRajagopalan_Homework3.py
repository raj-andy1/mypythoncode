"""
Homework 3- Anandthirth Rajagopalan
"""
def calculatePay(nuOfHrs, payRate):
    if nuOfHrs <= 40:
        #print ("nu of hrs < 40", nuOfHrs)
        totalPay = nuOfHrs * payRate
    elif nuOfHrs <=60:
        #print ("nu of hrs <60 but > 40", nuOfHrs)
        totalPay = 40 * payRate + (nuOfHrs - 40) * 1.5 * payRate
    else: # nu of hrs worked is > 60
        #print ("nu of hrs > 60",nuOfHrs)
        totalPay = 40 * payRate + 20 * 1.5 * payRate + (nuOfHrs - 60) * 2 * payRate

    return totalPay


print (calculatePay (20,30))
print (calculatePay (50,15.50))
print (calculatePay (70.25,11))

timeWorked = float(input("Enter the amount of time worked"))
rateOfPay = float(input("Enter the rate per hour paid"))
print ("Total amount to be paid is $" + str(calculatePay (timeWorked, rateOfPay)))
