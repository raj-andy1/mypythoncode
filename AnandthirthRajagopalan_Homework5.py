"""
Homework5 - Anandthirth Rajagopalan
"""
total = 0
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
    myNumList.append(userNum)
    #print (myNumList)
    #print (len(myNumList))
#Calculate total of all numbers and print each number    
for num in myNumList:
    print (num)
    total += num
avg = total / len(myNumList)
#Calculate least number
minNm = myNumList[0]
for num in myNumList:
    if num < minNm:
        minNm = num
#Calculate largets number
maxNm = myNumList[0]
for num in myNumList:
    if num > maxNm:
        maxNm = num

print ("Total is",total)
print ("Average is",avg)
print ("Least number is",minNm)
print ("Greatest number is",maxNm)
print ("OK Bye")
