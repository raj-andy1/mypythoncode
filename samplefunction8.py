"""
sampleFunction5 class3
absolute value
"""

def absoluteValue(valueIn):
    if valueIn >= 0:
        valueOut = valueIn
    else: #valueIn was -ve
        valueOut = -1 * valueIn

    return valueOut

print(absoluteValue(-3))
print(absoluteValue(4))
print(absoluteValue(0))
print(absoluteValue(1.345))
print(absoluteValue(-7.89))
    
