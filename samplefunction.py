"""
sampleFunction py file
"""
def showSeparator():
    print ("*******")
    print()
    
def getGroceries(item1, item2, item3, item4):
    print (item1)
    print (item2)
    print (item3)
    print (item4)
    showSeparator()

getGroceries('jello','muffins','milk','coffee')
getGroceries('banana','apples','grapes','pears')
getGroceries('tooty fruity','chocolate chips','shaved almonds','pecans')

needToBuy = input("What should we buy?")
alsoNeedToBuy = input("What esle do you need to buy?")

getGroceries ('wine',needToBuy, alsoNeedToBuy, 'champagne')
        
