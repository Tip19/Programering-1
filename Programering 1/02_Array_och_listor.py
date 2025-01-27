num = 0

toys = [
    "teddy bear", "toy train", "nerf gun", "super soaker", "xbox"
]
namn = [
    "Elis", "Adrian", "Linus", "Lukas", "Yunus"
]
number = [
    1, 2, 3, 4, 5,
]

cities = [

]
while True:
    Get_City = input ("please say the name of a city\nAnswer:").lower()
    if Get_City == "exit":
        break
    elif Get_City != "exit":
        cities.append(Get_City)
for item in cities:
    print (cities[num])
    num +=1


#for item in toys:
#    print (namn[num], "ger", toys[num], number[num])
#    num +=1



