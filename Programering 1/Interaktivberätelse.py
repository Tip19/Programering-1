import time
while True: #loop som repeatar om man ger ett ojiltigt svar
    print("\n\n\nDu vaknar i en skog men kommer ej ihåg varför eller hur du hamnade här\n\n")
    time.sleep(2)
    print ("Det ser ut som att du bara kan gå antingen syd eller nord, vilken riktning väljer du?")
    start = input ("svar: ").lower
    if start == "nord".lower:
        print("Du börjar att gå norrut tills du möter på en stig")
        break
    elif start == "syd".lower:
        print("Du valde att gå söderut.")
        break
    else:
        print("Ogiltigt svar. Du måste välja antingen 'nord' eller 'syd'. Försök igen.")
time.sleep(1)

while start == "nord".lower: #loopar om man väljer fel svar samt kod för om man skrev nord på linje 6
    nord = input ("\n\nDu kan antingen ta stigen eller gå nord\nSvar:") #checkar om man valde att gå på stigen
    if nord == "ta stigen".lower or "stigen".lower: 
        print("Du tar stigen som visar sig leda till en nära by där de ger dig vatten, mat och någonstans att stanna under natten\n\n")
        time.sleep(5)
        print("slut")
        break #slutar loopen
    elif nord == "gå nord".lower or "norr" or "nord".lower: # checkar om man valde att gå norr
        print("Du fortsätter nord men allting ser bara likadant\n\n")
        time.sleep(1)
        print("Du fortsätter längre in i skogen tills det börjar regna där du hittar en gråtta när\n\n")
        time.sleep(1)
        print ("du sätter äger i gråttan och gjör dig redo för dagen imorgon")
        time.sleep(2)
        print ("slut")
        break #slutar loopen
    else: #loopar tillbaka till linje 17
        print ("ogiltigt svar du måste välja antingen 'gå nord' eller 'ta stigen'")
    
