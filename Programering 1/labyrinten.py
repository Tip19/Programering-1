Room = 2
def room_designation(Room): #prints what room you are in and inquires if you want to go right or left
    print (f"You are in room: {Room}")
    return input("Where do you want to go: right or left? ").lower()

def try_again(): #prints that the user has done an invalid input and let's them try again
    return input ("Invalid input please try again \n")

while Room != "exit": #loops until the user has found the exit
    where = room_designation(Room)
    
    if where == "right" and Room < 4: #checks what direction the user went
        Room += 1 #changes the int of room +1 when moving to the right
        
    elif where == "left" and Room > 1: #checks what direction the user went
        Room -= 1 #changes the int of room -1 when moving to the left
    else:
        try_again()
        continue
    
    if Room == 3: #checks if you are in room 3
        print (f"You are in room: {Room}")
        Room_3 = input ("Where do you want to go: left or right or to the exit? ").lower()
        if Room_3 == "exit": #checks if you choose to go through the exit
            print ("you found the exit!")
            break #breaks loop
        elif Room_3 == "left":
            Room-=1
        elif Room_3 == "right":
            Room+=1
        else:
            try_again()
            continue
    
    if Room == 5: #if the player tries to go more right than room 4 (the furtherst room to the right)
         where = input ("you can't go further right, do you want to go left? ").lower() #tells the player they cant go any fruther right
         if where == "left": #checks if the player tries to go left
             room_designation(Room) #check line 2
    elif Room == 1: #if the player tries to go more left than room 1 (the furthest room to the left)
         where = input ("you can't go further left do you want to go left? ").lower()
    else:
         try_again()
         continue
