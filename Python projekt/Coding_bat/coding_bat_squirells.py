weekend = input("Is it a weekend?")
cigars = int(input("how many cigars are there at the party?"))
if cigars < 40 or cigars > 60 and weekend != "Yes" or "yes":
    print ("False")
elif cigars > 40 and cigars < 60:
    print ("True")

