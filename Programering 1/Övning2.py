mil2 = int(input("Mätarställning i dag? "))
mil1 = int(input("Mätarställning för ett år sedan? "))
if mil2 < mil1: 
    print ("fel number inmatade")
else:   
    print("Antal körda mil:", mil2 - mil1)
    liter = float(input("Antal liter bensin? "))
    print(f"Förbrukning per mil: {liter / (mil2 - mil1):.2f}")