import time
börja_om = True
pengar = 10
# Quiz frågorna 
quiz_questions = [
    "Vad är huvudstaden i Sverige? ",
    "Vilken planet är känd som den röda planeten? ",
    "I vilken sport tävlar man i Tour de France? ",
    "Vad heter den längsta floden i världen? ",
    "Vem var den första presidenten i USA? ",
    "Vilket år inträffade den franska revolutionen? ",
    "Vad är den kemiska formeln för vatten? ",
    "Vilken gas utgör majoriteten av jordens atmosfär? ",
    "Vad står förkortningen AI för? ",
    "Vem sjunger låten Shape of You? ",
]

# Quiz svar
quiz_answer = [
    "stockholm",
    "mars",
    "cykling",
    "nilen",
    "george washington",
    "1789",
    "h2o",
    "kväve",
    "artificial intelligence",
    "ed sheeran",
]

# definition för rätt svar
def right_answer(fråga, poäng, runda):
    print ("du har rätt")
    fråga +=1
    runda +=1
    poäng +=1
    time.sleep(1)
    print (f"du har {poäng} poäng")
    return fråga, poäng, runda

# definiton för fel svar    
def wrong_answer(fråga, poäng, runda):
    print ("du har fel")
    fråga +=1
    runda +=1
    time.sleep(1)
    print (f"du har {poäng} poäng")
    return fråga, poäng, runda

def kör_igen(börja_om):
    börja_om = input ("vill du köra igen? ")
    if börja_om == "ja":
        börja_om = True
    elif börja_om == "nej":
        börja_om = False
    return börja_om


while börja_om:
    fråga = 0
    poäng = 0
    runda = 0

    #kollar om du vill betta        
    betting = input ("vill du betta om du kommer få över 50% poäng: ja/nej")
    if betting == "ja":
        betting_amount = int(input ("hur mycket vill du betta? ")) # kollar hur mycket du vill betta
        while betting_amount > pengar or betting_amount <= 0:# ser till att du inte försöker betta mer än vad du har
            betting_amount = int(input (f"Du har inte {betting_amount} pengar du har {pengar} pengar, hur mycket vill du betta? "))

    #kör i 10 runder
    while runda < 10:
        quiz = input(quiz_questions[fråga]).lower() # printar frågan
    
        if quiz == quiz_answer[fråga]: # kollar om de svarat rätt
            fråga, poäng, runda = right_answer(fråga, poäng, runda) # kör definitionen right_answer

        elif quiz != quiz_answer[fråga]: # kollar om de svarat fel
            fråga, poäng, runda = wrong_answer(fråga, poäng, runda) # kör definitonen wrong_answer

    if runda == 10 and poäng >= 5: # kollar om de vann
        print (f"Bra gjort du vann du fick minst 50 procent rätt, totalt fick du {poäng} poäng")
        if betting == "ja":
            pengar += betting_amount # ger rätt mängd pengar om de vann
        time.sleep(1)
        print (f"Du har totalt {pengar} pengar")
        börja_om, kör_igen(börja_om)
    elif runda == 10 and poäng < 5: # kollar om de förlorade
        print (f"Du förlorade du fick under 50 procent poäng, totalt fick du {poäng} poäng")
        if betting == "ja":
            pengar -= betting_amount # tar rätt mängd pengar om de förlorade
        time.sleep(1)
        print (f"du har totalt {pengar} pengar")
        börja_om, kör_igen(börja_om)
    
    # kollar om de vill köra igen