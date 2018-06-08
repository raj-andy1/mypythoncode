"""
Homework5 - Anandthirth Rajagopalan
"""
total = 0
minNm = 0
maxNm = 0
myNumList = []

while True:
    userNum = input("Enter a number:")
    if userNum == '':
        break
    try:
        userNum = float(userNum)
    except:
        print("That's not an integer")
        continue
    myNumList.append(float(userNum))
    #print (myNumList)
    #print (len(myNumList))
#Calculate total of all numbers and print each number    
for num in myNumList:
    print (num)
    total += num
avg = total / len(myNumList)
#Calculate least number
for num in myNumList:
    if num < minNm:
        minNm = num
for num in myNumList:
    if num > maxNm:
        maxNm = num

print ("Total is",total)
print ("Average is",avg)
print ("Least number is",minNm)
print ("Greatest number is",maxNm)
print ("OK Bye")
