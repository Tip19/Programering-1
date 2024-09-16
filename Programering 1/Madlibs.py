import time

print("Skriv ett ord som korrelerar med följande instruktion\n")
instruc = ["ett djur", "en färg", "ett tal"]
array = []

for i in range(len(instruc)):
    namn = input(instruc[i] + ": ")
    array.append(namn)

print (array[0] + " gick genom den " + array[1] + " skogen.\n Efter " + array[2])
