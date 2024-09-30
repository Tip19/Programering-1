import time

Room = 2 #defines room as 2
key = 0
room_array = ["Old weapons and armor lie scattered. Beneath a loose stone, a small iron key waits to be found.", "You start in a damp, narrow corridor. Flickering torchlight barely illuminates the uneven stone floor.", "A heavy stone door blocks the exit. It’s locked, but a keyhole glimmers, offering a way out.", "An empty, echoing room with faded murals and dripping water. The silence is almost oppressive."]
def room_designation(Room): #prints what room you are in and inquires if you want to go right or left
    print (f"You are in room: {Room}")
    return input("Where do you want to go: right or left? ").lower()

def key_def():
    print (f"you are in room: {Room}")
    print (room_array[0])
    time.sleep(2)
    return input ("what do you want to do: left or right or pick up key? ").lower()

def try_again(): #prints that the user has done an invalid input and let's them try again
    return input ("Invalid input please try again \n")

while Room != "exit": #loops until the user has found the exit
    if Room == 2:
        print (room_array[1])
        time.sleep(2)
    
    if Room == 4:
        print (room_array[3])
        time.sleep(2)

    where = room_designation(Room)

    if where == "right" and Room < 4: #checks what direction the user went
        Room += 1 #changes the int of room +1 when moving to the right
        
    elif where == "left" and Room > 1: #checks what direction the user went
        Room -= 1 #changes the int of room -1 when moving to the left
    else:
        try_again()
        continue

    if Room == 1:
        key_room = key_def()
        if key_room == "pick up key" or key_room == "pick up" and key == 0:
            print ("you pick up the key")
            key += 1
        elif key_room == "right":
            Room += 1
        elif key_room == "left":
            Room -= 1

    if Room == 3: #checks if you are in room 3
        print (room_array[2])
        time.sleep(2)
        print (f"You are in room: {Room}")
        time.sleep(1)
        Room_3 = input ("Where do you want to go: left or right or to the exit? ").lower()
        if Room_3 == "exit" and key == 1: #checks if you choose to go through the exit
            print ("you found the exit!")
            break #breaks loop
        elif key == 0 and Room_3 == "exit":
            print ("you try to open the exit but the door is locked")
            time.sleep(1)
        elif Room_3 == "left":
            Room-=1
        elif Room_3 == "right":
            Room+=1
        else:
            try_again()
            continue