import time
import random

score = 0
round = 0

while True:
    try:
        rounds = int (input ("how many rounds do you want to play\nAnswer:"))
        break
    except ValueError:
        time.sleep(1)
        print ("\nplease only input a number")

while round <= rounds - 1:
    Rps = int (input ("choose rock, paper or scissors by typing 1, 2 or 3: "))
    npc_choice = random.randint (1,3) # 1 = rock 2 = paper 3 = scissors
    if Rps - npc_choice == 0:
        print ("its a tie")
    elif Rps - npc_choice == 1 or -2:
        print ("you win")
        score +=1
    else:
        print ("you lose")
    round += 1
print (f"you won {score} times")