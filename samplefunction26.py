"""
sample function26 - class 6
"""

monthNm = int(input('Enter a number from 1 to 12:'))
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
monthAb = months[(monthNm-1)*3:((monthNm-1)*3)+3]

print ('Month Abbrev',monthAb)
