#quiz app
fråga = 0
poäng = 0
runda = 0
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

def right_answer(fråga, poäng, runda):
    print ("du har rätt")
    fråga +=1
    runda +=1
    poäng +=1
    print (f"du har {poäng} poäng")
    return fråga, poäng, runda
    
def wrong_answer(fråga, poäng, runda):
    print ("du har fel")
    fråga +=1
    runda +=1
    print (f"du har {poäng} poäng")
    return fråga, poäng, runda


while runda < 10:
    quiz = input (quiz_questions[fråga]).lower()

    if quiz == quiz_answer[fråga]:
        fråga, poäng, runda = right_answer(fråga, poäng, runda)
    elif quiz != quiz_answer[fråga]:
        fråga, poäng, runda = wrong_answer(fråga, poäng, runda)