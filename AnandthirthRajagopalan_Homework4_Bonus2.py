"""
Homework4 - Bonus2 - Anandthirth Rajagopalan
"""
import random

def countChange(nQ,nD,nN,nP):
    totalCash = nQ * .25 + nD * .10 + nN * .05 + nP * 0.01
    return totalCash

while True:
    userName = input("Enter your name(Hit Return/Enter to quit):")
    if userName == '' or userName == 'q':
        print ("OK bye")
        break
    nuOfQ = int(input("Enter the amount of quarters:"))
    nuOfD = int(input("Enter the amount of dimes:"))
    nuOfN = int(input("Enter the amount of nickels:"))
    nuOfP = int(input("Enter the amount of pennies:"))
    nuOfCe = round((countChange(nuOfQ,nuOfD,nuOfN,nuOfP) % 1) * 100)
    nuOfDo = int(countChange(nuOfQ,nuOfD,nuOfN,nuOfP))
    print ("All counted",userName, "has $" + \
           str(nuOfDo),"and", nuOfCe, "cents")
    mesgNu = 0
    mesgNu = random.randrange(1,4)
    if mesgNu == 1:
        print ("Woot, Woot!!!")
    elif mesgNu == 2:
        print ("You can certainly do better!!")
    else:
        print ("Hit the gas pedal on saving!!")

                
    
        
