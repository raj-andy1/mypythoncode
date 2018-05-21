"""
samplefunction7 class3
return a string -ve,+ve or 0
"""

def returnValue(number):
    if number > 0:
        strout = "Positive"
    elif number < 0:
        strout = "Negative"
    elif number == 0:
        strout = "Zero"
    else: #invalid number
        strout = "Invalid"

    return strout

print (returnValue(5))
print (returnValue(-10))
print (returnValue(0))
print (returnValue(-9.4))
