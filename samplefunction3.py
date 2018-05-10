"""
sampleFunction3 py file
calculate the average of 3 numbers
"""

def average(value1, value2, value3):
    total = value1 + value2 + value3
    theAverage = total / 3.0
    #print ("The average of" ,value1, value2, value3, "is:",theAverage)
    return (theAverage)


avg1 = average (10,11,12)
print (avg1)
avg2 = average (1.5,2.5,3.5)
print (avg2)
avg3 = average (-55.7,-20.3,-45.6)
print (avg3)

userNumber1 = input("Enter a number:")
#userNumber1 = float(userNumber1)
userNumber2 = input("Enter a second number:")
#userNumber2 = float(userNumber2)
userNumber3 = input("Enter a third number:")
#userNumber3 = float(userNumber3)

avg4 = average (float(userNumber1), float(userNumber2), float(userNumber3))
print (avg4)
