#GUESS MY NUMBER 
import random

num = random.randint(0,100)

def guessing():
    guess = int(input('Guess the number: '))
    chance = 0
    while chance != 7:
        chance += 1
        if guess < num:
            print('Higher...')
            guess = int(input('Guess the number: '))
        elif guess > num:
            print('Lower...')
            guess = int(input('Guess the number: '))
        else:
            print('Correct!')

def display_num_info():
    print('''I have selected a number between 1 and 100.
                You have 7 chances to get it
    ''')

display_num_info()
guessing()

input('Press enter to exit') 
    
        


