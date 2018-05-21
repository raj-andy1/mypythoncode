"""
samplefunction10 class3
calculate shipping costs
"""

def calculateShipping(country, widgets):
    if country == 'USA' or country == 'US':
        if widgets <= 50:
            cost = 6.25
        elif widgets <= 100:
            cost = 9.50
        elif widgets <= 150:
            cost = 12.75
        else:
            cost = 15.00
    elif country == 'Canada' or country == 'CAN':
        if widgets <= 50:
            cost = 8.25
        elif widgets <= 100:
            cost = 12.50
        elif widgets <= 150:
            cost = 18.00
        else:
            cost = 25.00
    else:
        cost = 'Not Yet'

    return cost

print(calculateShipping('US', 125))
print(calculateShipping('CAN', 80))
print(calculateShipping('USA',200))
print(calculateShipping('Canada',10))
        
