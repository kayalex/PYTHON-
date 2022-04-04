#Guess my number
#
#The computer picks a random number between 1 and 100,
#then the player tries to guess it and the computer
#lets the player know if its too high or too low!!!

import random

print("\tWelcome to Guess My Number")
print("\t\tI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as poossible.\n")
#Set the initial values
the_number = random.randrange(100) + 1
guess = int(input("Take a guess:"))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higer...")

    guess = int(input("Take a guess:"))
    tries += 1
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And you did it in", tries , "tries")

    if tries == 8:
        print("Game over")
        print("you failed, the number was", the_number)
        break
    

input(" press enter key to exit")


   
