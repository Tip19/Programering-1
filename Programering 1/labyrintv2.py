import time

# Variables
Room = 2  # Current room number
key = 0  # Key status: 0 = not picked up, 1 = picked up
room_array = [
    "Old weapons and armor lie scattered. Beneath a loose stone, a small iron key waits to be found.",
    "You start in a damp, narrow corridor. Flickering torchlight barely illuminates the uneven stone floor.",
    "A heavy stone door blocks the exit. It’s locked, but a keyhole glimmers, offering a way out.",
    "An empty, echoing room with faded murals and dripping water. The silence is almost oppressive.",
    "Rough, damp walls with moss and hanging stalactites. A shallow pool reflects the faint sound of dripping water."
]

# Function Definitions
def room_designation(Room):
    # Display the current room and ask the player for their direction choice
    print(f"You are in room: {Room}")
    return input("Where do you want to go: right or left? ").lower()

def key_def():
    # Display the contents of room 1 and ask the player what they want to do
    print(f"You are in room: {Room}")
    print(room_array[0])  # Description of room 1
    time.sleep(2)  # Pause to allow player to read
    return input("What do you want to do: left, right, or pick up key? ").lower()

def try_again():
    # Prompt the user to try again after an invalid input
    return input("Invalid input, please try again \n")

# Game Loop
while Room != "exit":
    if Room == 2:
        print(room_array[1])  # Description of room 2
        time.sleep(2)

    if Room == 4:
        print(room_array[3])  # Description of room 4
        time.sleep(2)

    if Room == 5:
        print(room_array[4])
        time.sleep(2)

    # Get the player's direction choice
    where = room_designation(Room)

    # Move the player based on their choice
    if where == "right" and Room < 5:
        Room += 1  # Move right to the next room
    elif where == "left" and Room > 1:
        Room -= 1  # Move left to the previous room
    else:
        try_again()  # Handles invalid direction
        continue

    # Handles actions in room 1 (where the key is located)
    if Room == 1:
        key_room = key_def()  # Gets the player's action in room 1
        if key_room == "pick up key" or (key_room == "pick up" and key == 0):
            print("You pick up the key.")
            key += 1  # Update key status to picked up
        elif key_room == "right":
            Room += 1  # Move right to room 2
        elif key_room == "left":
            Room -= 1  # Move left to room 0

    # Handles actions in room 3 (where the exit is located)
    if Room == 3:
        print(room_array[2])  # Description of room 3
        time.sleep(2)
        print(f"You are in room: {Room}")
        time.sleep(1)
        Room_3 = input("Where do you want to go: left, right, or to the exit? ").lower()
        
        if Room_3 == "exit" and key == 1:
            print("You found the exit!")
            break  # Exit the game
        elif key == 0 and Room_3 == "exit":
            print("You try to open the exit, but the door is locked.")
            time.sleep(1)
        elif Room_3 == "left":
            Room -= 1  # Move left to room 2
        elif Room_3 == "right":
            Room += 1  # Move right to room 4
        else:
            try_again()  # Handle invalid input
            continue
