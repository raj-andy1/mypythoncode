"""
sampleprogram16 - class4
flip a coin
"""
import random

maxFlips = int(input("How many flips to do?"))

nuOfFlips = 0
nuOfTails = 0
nuOfHeads = 0

while nuOfFlips < maxFlips:
    zeroOrOne = random.randrange(0,2)
    if zeroOrOne == 1:
        nuOfHeads += 1
    else:
        nuOfTails += 1
    nuOfFlips += 1

print("Flipping a coin",maxFlips,"times, you got", nuOfHeads, \
      "Heads and",nuOfTails,"Tails")

