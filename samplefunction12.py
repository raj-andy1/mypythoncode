"""
samplefunction9 class 3
is it a rectangle?
"""

def isRect(left, top, right, bottom):
    if left == right and top == bottom:
        strOut = True
    else:
        strOut = False

    return strOut

print(isRect(5,4,5,4))
print(isRect(1,2,3,4))
print(isRect(4,8,9,3))
