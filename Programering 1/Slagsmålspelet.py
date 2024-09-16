import time
import random
coin = 10
play_again = True
name_p1 = input("Input name: ").lower()
while len(name_p1) < 3 or len(name_p1) > 8: # checks so name is between 3 and 8 characters
    name_p1 = input("Input a name between 3 and 8 characters long: ")

while play_again: # Reset HP for both players at the start of each game
    player1_hp = 100 #hp for player one
    player2_hp = 100 #hp for player two
    lost_bet = 0
    won_bet = 0
    rounds = 10 # how many rounds before a tie

    #betting
    betting = input ("Do you want to bet money on who is going to win? yes/no\n").lower() #checks if you want to bet money on who wins
    while betting != 'yes' and betting != 'no': # repeats question if you answered something different than yes or
        betting = input ("Do you want to bet money on who is going to win? yes/no\n").lower()
    if betting == 'yes':
        betting2 = input ("Do you want to bet on if you win or lose?\n").lower()
        while betting2 != 'win' and betting2 != 'lose':
            betting2 = input ("Do you want to bet on if you win or lose?\n").lower()

        if betting2 == 'win':
            while True:
                try:
                    win_betting = int(input(f"How much do you want to bet current coin balance {coin}\n")) #f string showing how much money you have
                    break
                except ValueError: # checks so the user puts in a int
                    print ("incorrect input, please enter a number")
            won_bet = 1 # updates variable for later use so the program knows what you betted 
            while win_betting > coin or win_betting < 0: # make sure you can bet the amount you wrote
                while True:
                    try:
                        win_betting = int(input("you do not have enough coins for that, bet another amount: "))
                        break
                    except ValueError:
                        print ("incorrect input please enter a number")
            coin -= win_betting

        elif betting2 == 'lose': # loop to make sure it's a int
            while True:
                 try:     
                    lose_betting = int(input(f"How much do you want to bet current coin balance {coin}\n")) # f string showing how much money you have
                    coin -= lose_betting
                    break
                 except ValueError: # cheks so the user puts in a int
                    print("incorrect value, please enter a number")
            lost_bet = 1 # updates variable for later use so the program knows what you betted
            while lose_betting > coin or lose_betting < 0:
                while True:
                    try:
                        lose_betting = int(input("you do not have enough coins for that, bet another amount: "))
                        break
                    except ValueError:
                        print ("Incorrect value, please enter a number")


    for round_number in range (1, rounds + 1):  # loop runs combat choosing random ints and subtracting it from player hp
        print (f"round:{round_number}")
        time.sleep(1)
        if player1_hp <= 0 or player2_hp <= 0: # breaks loop if either hp is under or equals 0
            break
        # combat for the player
        hit_punch_pc = random.randint(1,5)
        hit_kick_pc = random.randint(1, 2) # randomizer if the players attack will hit or not
        combat = input ("Do you want to punch or kick?\n").lower()  #Let's the player decide if they want to punch or kick
        if combat == 'kick' and hit_kick_pc == 1: #checks for if the player wants to kick and if it is a hit or not
            player2_hp -= random.randint(0, 40) # kick damage
        
        elif combat == 'punch' and hit_punch_pc in (1,4):
            player2_hp -= random.randint(10, 20) # punch damage
        while combat != 'kick' and combat != 'punch': # loops question on line 49 until gets a valid answer
            combat = input ("Do you want to punch or kick?\n").lower()

        # combat for npc
        npc_random_combat = random.randint(1, 2) #randomly chooses if the npc is going to punch or kick
        hit_kick_npc = random.randint (1,2)
        hit_punch_npc = random.randint(1,5)
        if npc_random_combat == 1 and hit_punch_npc in (1,4):
            player1_hp -= random.randint (10,20) # punch damage
            
        elif npc_random_combat == 2 and hit_kick_npc == 1:
            player1_hp -= random.randint (0, 40) # kick damage
        print(f"{name_p1}: {player1_hp}, Player 2 hp: {player2_hp}")  # prints the results of each round
        time.sleep(1)  # waits one second before restarting loop

    # checks for tie
    if player1_hp <= 0 and player2_hp <= 0:
        print("It is a tie")
        if lost_bet == 1: # checks what you betted
            coin = coin + lose_betting # gives back your coins on a tie
            print (f"your coin bablance is: {coin}")

        elif won_bet == 1: # checks what you betted
            coin = coin + win_betting # gives back your coins on a tie
            print (f"your current coin balance is: {coin}")

    # checks for npc win
    elif player1_hp <= 0:
        print("Player 2 is the winner")
        if won_bet == 1: # checks if the player was wrong in their betting
            time.sleep(1)
            print (f"your current coin balance is: {coin}")

        elif lost_bet == 1: # checks if the player was right in their betting
            coin = coin + lose_betting * 2 # gives double their bet back
            time.sleep(1)
            print (f"your current coin balance is: {coin}")

    # checks for player 1 win
    elif player2_hp <= 0:
        print(f"{name_p1} is the winner")
        if won_bet == 1: # checks if they betted to win
            coin = coin + win_betting * 2 # gives double their bet back
            time.sleep(1)
            print (f"your current coin balance is: {coin}")

    # checks if you want to play again
    play_again = input("Play again? yes/no\n").lower() 
    if play_again == 'no':
        print("Thanks for playing!")
        play_again = False  # Exit the loop
    elif play_again == 'yes':
        play_again = True  # Continue playing
    else:
        print("Invalid input, exiting the game.")
        break  # Exit the loop on invalid input