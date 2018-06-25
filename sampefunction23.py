"""
sample function 23 - class 5
"""

a = 0
b = 0
c = 0
d = 0

for a in range (0,10):
    #print ('a',a)
    for b in range (0,10):
        #print ('b',b)
        for c in range (0,10):
            #print ('c',c)
            for d in range (0,10):
                #print ('d',d)
                if (a ** 2 + b ** 2 == c **2 + d ** 2):
                    if a != b and b != c and c != d and d != a and a != c and b != d :
                        print (a, b, c, d)
