#choose random number
#let user guess what the number is
#tell user if their guess is too high or low or exactly right
#make sure program doesnt crash when someone puts in something not base 10 
import random

num = random.randint (1, 100)

while True:
    try:
        guessing = int(input ("Guess a number between 1 to 100\nAnswer: "))
        if guessing > num:
            print ("your guess is too high")
        elif guessing == num:
            print (f"you are correct the nubmer was {num}")
        elif guessing < num:
            print ("your guess is too low")
            break
    except ValueError:
        print("please only put in numbers")
