"""
samplefunction3 class 3
what to wear
"""

def whatToWear(temp):
    if temp > 90:
        clothes = 'swimwear'
    elif temp > 70:
        clothes = 'shorts'
    elif temp > 50:
        clothes = 'long pants'
    else: #its cold outside
        clothes = 'thermal underwear and long pants'

    return clothes

print ('Put on', whatToWear(50))
print ('Put on', whatToWear(100))
print ('Put on', whatToWear(20))
print ('Put on', whatToWear(85))


userTemp = int(input('What is the temperature today?'))
print ('Put on', whatToWear(userTemp))

        
