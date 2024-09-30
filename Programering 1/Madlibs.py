import time

print("Skriv ett ord som korrelerar med följande instruktion\n")
instruc = ["en plats", "en grej","ett adjektiv", "ett verb", "en till grej", ]
array = []

for i in range(len(instruc)):
    namn = input(instruc[i] + ": ")
    array.append(namn)

print ("En dag när jag gick genom " + array[0] + " såg jag plötsligt en " + array[1] + " som verkade väldigt " + array[2] + " Jag bestämde mig för att " + array[3] + " och undersöka vad som hade hänt. När jag närmade mig, insåg jag att " + array[0] + " var faktiskt en" + array[4] + " Det var en upplevelse som jag aldrig kommer att glömma.")
