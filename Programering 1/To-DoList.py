#This code allows you to have a To-Do list to remember the things you need to do, before running the code you can remove the things in the To_Do_list array 
import time

# Set the To-Do list with some example tasks
To_Do_list = [
    {"task": "homework"},
    {"task": "walk the dog"},
]

# Function to add a task to the To-Do list
def Add(Add_remove):
    if Add_Remove == "add": # Only runs if the user wants to add a task
        time.sleep(1)
        Add = input ("what do you want to add to your To-Do list?\nAnswer: ").lower()
        To_Do_list.append({"task": Add}) # Append the new task to the list
        return Add
    
# Function to remove task from the To-Do list
def Remove(Add_remove):
    if Add_Remove == "remove":
        time.sleep(2)
        print ("What do you want to remove from the list?")
        time.sleep(1)
        Remove = input ("\nAnswer: ").lower()

    # Checks if the task is in the To-Do list
    if {"task": Remove} in To_Do_list: 
        To_Do_list.remove({"task": Remove}) # Removes task from list (Help with syntax by AI)
        return Remove
    else:
        time.sleep(2)
        print ("\nthis task is not in your To-Do list")

# Main loop that displays the list and allows the user to add or remove tasks
while True:

    # Prints each item in the list(Help with syntax by AI)
    for item in To_Do_list:
     time.sleep(1)
     print(f"To-Do list: {item['task']}\n")
     time.sleep(1)

     # Ask the user if they want to add or remove a task
    Add_Remove = input ("do you want to add or remove something from your To-Do list or are you done?\nAnswer: ").lower()

    # Exits the loop if the user is finished
    if Add_Remove == "no" or "done":
        break
    # Calls the right function depending on what the users choice
    elif Add_Remove == "add":
        Add(Add_Remove)
    elif Add_Remove == "remove":
        Remove(Add_Remove)
    else:
        print ("Invalid input please type add or remove or done")
