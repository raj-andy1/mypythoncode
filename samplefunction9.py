"""
samplefunction 6 class3
is it a square
"""

def isSquare(length, width):
    if length == width:
        valueOut = True
    else:
        valueOut = False

    return valueOut

print (isSquare(5,4))
print (isSquare(4,4))
print (isSquare(-5,7))
