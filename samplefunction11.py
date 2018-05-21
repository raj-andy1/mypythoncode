"""
samplefunction8 class3
return if a number is even or odd
"""
def returnEO(number):
    if number % 2 == 0:
        strout = "Even"
    else:
        strout = "Odd"

    return strout

print (returnEO(5))
print (returnEO(6))
print (returnEO(-4))
print (returnEO(-1.2))
