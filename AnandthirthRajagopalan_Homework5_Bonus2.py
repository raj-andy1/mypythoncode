"""
Homework5 - Bonus2 - Anandthirth Rajagopalan
"""
import random
myCards = []
cardNumber = ['Ace','2','3','4','5','6','7','8','9','10','Queen','King','Jack']
suitName = ['Spades','Hearts','Clubs','Diamonds']

for suit in suitName:
    for card in cardNumber:
        cardNm = card + ' ' + 'of' + ' ' + suit
        myCards.append(cardNm)
        print (cardNm)
#print ('All the cards in the deck are',myCards)
random.shuffle(myCards)
print ('Shuffled deck of Cards',myCards)
