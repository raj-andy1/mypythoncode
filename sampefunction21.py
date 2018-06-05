"""
samplefunction 21 - Class 5
Madlibs
"""
import random

nmList = ['Andy Raj','Gowri Rao','Amogh Rao','Vijaya K','Krishnamurty R',\
          'Sangeetha G','Govindarajan L','Aburva GS','Abhinav KGS']
verbList = ['ran','ate','choked','punched','learnt','blinked','sighed','closed']
adjList = ['aggressive','beautiful','ugly','dominant','brave']
nounList = ['basketball','tennisball','baseball','football']
#nNm = len(nmList)

while True:
    #name = input('Enter a name:')
    name = nmList[(random.randrange(0,len(nmList)))]
    verb = verbList[(random.randrange(0,len(verbList)))]
    adjective = adjList[(random.randrange(0,len(adjList)))]
    noun = nounList[(random.randrange(0,len(nounList)))]
    #print (name)
    #verb = input('Enter an action:')
    #adjective = input('Enter an adjective:')
    #noun = input('Enter a noun:')

    sentence = name + ' ' + verb + ' ' + 'down the hill hoping to escape the' \
               + ' ' + adjective + ' ' + noun + '.'
    print ('###')
    print (sentence)
    print ('###')
    goAgain = input ('Enter/Return to continue, anything else to quit')
    if goAgain != '':
        break

print ('OK, Bye')
