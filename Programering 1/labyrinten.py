Room = 2
def room_designation(Room):
    print (f"You are in room: {Room}")
    return input("Where do you want to go: right or left? ").lower()

def try_again(): 
    return input ("Invalid input please try again \n").lower()

while Room != "exit":
    where = room_designation(Room)
    
    if where == "right":
        Room += 1
        
    elif where == "left":
        Room -= 1
    else:
        try_again()
        continue
    
    if Room == 3:
        print (f"You are in room: {Room}")
        Room_3 = input ("Where do you want to go: left or right or to the exit? ").lower()
        if Room_3 == "exit":
            print ("you found the exit!")
            break
        elif Room_3 == "left":
            Room-=1
        elif Room_3 == "right":
            Room+=1
        else:
            try_again()
            continue
    
    if Room == 4:
         where = input ("you can't go further right, do you want to go left? ").lower()
         if where == "left":
             room_designation(Room)
    elif Room == 0:
         where = input ("you can't go further left do you want to go left? ").lower()
    else:
         try_again()
         continue