#Word Jumble Game
#=================
import random
print('Welcome to the word jumble game!!!')
WORDS = ('aeroplane', 'helicopter', 'subway', 'minibus', 'airport', 'station', 'house', 'photosynthesis', 'chicken', 'sausage')
lives = 5
while lives != 0:
    word = random.choice(WORDS)
    correct = word

    jumble = ''
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    # print("""
    #         Welcome to the word jumble game!

    # ENJOY
    # """)
    print('ypur word to guess is: ', jumble)
    guess = input('Enter your guess of the word: ')
    while guess != correct:
        print('Nope, you got it wrong')
        print('heres the word once more: ', jumble)
        guess = input('Try again: ')
        lives += -1
    if guess == correct:
        print('CONGRATULATIONS!!! Youn got the word right.')

input('press enter to exit')   
