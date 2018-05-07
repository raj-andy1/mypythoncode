#example to calculate and print paycheck

rate = 10.00
totalHours = 55
regularHours = 40

overtimeHours = totalHours - regularHours
earnings = (regularHours * rate )+ (overtimeHours * rate * 1.5)
print ('I worked', totalHours,'hours. Hence I should be paid $',earnings) 
