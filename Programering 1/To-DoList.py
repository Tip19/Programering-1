import time
To_Do_list = [ # stores the list of tasks 
    {"task": "homework"},
    {"task": "walk the dog"},
]

#lets user add something to their list
def Add(Add_remove):
    if Add_Remove == "add": # runs code below only if the user wants to add something to the To-Do list
        time.sleep(1)
        Add = input ("what do you want to add to your To-Do list?\nAnswer: ").lower()
        To_Do_list.append({"task": Add}) # Adds the item to their To-Do list (Help with syntax by AI)
        return Add
    
# lets user remove something from their list
def Remove(Add_remove):
    if Add_Remove == "remove":
        time.sleep(2)
        print ("What do you want to remove from the list?")
        time.sleep(1)
        Remove = input ("\nAnswer: ").lower()
    if {"task": Remove} in To_Do_list: # Checks if the item the user wants to remove is in the list
        To_Do_list.remove({"task": Remove}) # (Help with syntax by AI)
        return Remove
    else:
        time.sleep(2)
        print ("\nthis task is not in your To-Do list")

# prints the list and asks if you want to add or remove something
while True: # loops until the user is either done adding or removing from their list
    for item in To_Do_list: # runs until every item is printed in the list
     time.sleep(1)
     print(f"To-Do list: {item['task']}\n") # prints each item in the list(Help with syntax by AI)
     time.sleep(1)
    Add_Remove = input ("do you want to add or remove something from your To-Do list or are you done?\nAnswer: ").lower()
    if Add_Remove == "no" or "done":
        break
    elif Add_Remove == "add":
        Add(Add_Remove)
    elif Add_Remove == "remove":
        Remove(Add_Remove)
