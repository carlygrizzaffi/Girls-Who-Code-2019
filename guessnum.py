#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    print("That's not a positive whole number, try again!")
else:
    guess = int(guess) # converts a string to an integer

if aRandomNumber == guess:
    print("You guessed correctly!")
else:
    print("Guess again!")

while aRandomNumber != guess:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    guess = int(guess)
    if guess == aRandomNumber:
        print("You guessed correctly!")
    else:
        print(guess == aRandomNumber)
        print("Guess again!")