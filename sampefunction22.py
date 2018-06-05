"""
sample function 22 - Class 5
"""

nmList = ['Andy Raj','Gowri Rao','Amogh Rao','Vijaya K','Krishnamurty R',\
          'Sangeetha G','Govindarajan L','Aburva GS','Abhinav KGS']

for name in nmList:
    print (name)

friendList = ['Chandru','Vinod','Varun','Karthick']

for friend in friendList:
    message = 'Happy New Yr' + ' ' + friend
    print (message)

numList = [21,45,87,90,78,76,77]
for num in numList:
    print ('The next number is',num)

total = 0
for num in numList:
    total = num + total
print ('Total is', total)
