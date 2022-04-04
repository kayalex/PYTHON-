
import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

count = 0
while count != 100:
    dice = random.randint(1,6)
    count += 1
    if dice == 1:
        print("1")
        one += 1
    elif dice == 2:
        print("2")
        two += 1
    elif dice == 3:
        print("3")
        three += 1
    elif dice == 4:
        print("4")
        four += 1
    elif dice == 5:
        print("5")
        five += 1
    elif dice == 6:
        print("6")
        six += 1
        
print("We rolled a dice 100 times and got", one, "ones", two, "twos",three, "threes" ,four, "fours", five,"fives","and", six, "sixes")

input("Press enter to exit")
    
