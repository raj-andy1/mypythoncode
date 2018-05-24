"""
sampleprogram19 - class4
guess the number
"""

#Show Introduction
print("This is the guess the correct number program")
print("Guess any number between 1 and 20")
print("You have 5 guesses")

import random


def playOneRound():
    ranTarget = 0
    guessNum = 0
    ranTarget = random.randrange(1,21)

    while True:
        userGuess = input("Enter a number between 1 and 20")
        guessNum += 1
        try:
            userGuess = int(userGuess)
        except:
            print("Thats not an integer")
            continue
        if userGuess == ranTarget:
            print("You guessed correct")
            print("You got it in", guessNum,"guesses")
            break
        elif userGuess < ranTarget:
            print (" you guess is low")
        else:
            print ("Your guess is high")
            
        if guessNum == 5:
            print("you are done guessing")
            print("Correct answer is",ranTarget)

while True:
    playOneRound()
    goAgain = input("Enter to continue or q to quit")
    if goAgain == 'q':
        break
print("Bye")

