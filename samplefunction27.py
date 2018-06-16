"""
samplefunction27 -- class6
count char in string
"""

def countCharInStr(findChar, targetStr):
    count = 0
    for char in targetStr:
        if findChar == char:
            count += 1

    return count
        
def countSubstrInStr(findSubstr, targetStr):
    count = 0
    nCharInTargetStr = len(targetStr)
    nCharInFindStr = len(findSubstr)
    lastPossibleStartingIndex = (nCharInTargetStr - nCharInFindStr) + 1
    for startIndex in range(0,lastPossibleStartingIndex):
        subStr = targetStr[startIndex:(startIndex+nCharInFindStr)]
        #print (subStr)
        #print ('Start index',startIndex)
        #print ('End slice', startIndex+nCharInFindStr)
        if subStr == findSubstr:
            count += 1

    return count 
        


#print (countCharInStr('m','mississippi'))
#print (countCharInStr('i','mississippi'))
#print (countSubstrInStr('a','banana'))
print (countSubstrInStr('ana','banana'))
print (countSubstrInStr('ama', 'bananarama'))
print (countSubstrInStr('aaaaaaaaaaaaaa', 'bananarama'))
