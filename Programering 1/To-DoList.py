#displays list
# option to add things to list
# option to complete things on list and remove them
import time
To_Do_list = [
    {"task": "homework"},
    {"task": "walk the dog"},
]
def Edit_list(Add_remove):
    if Add_Remove == "add":
        time.sleep(1)
        Add = input ("what do you want to add to your To-Do list?\nAnswer: ").lower()
        To_Do_list.append(Add)
        return Add
    elif Add_Remove == "remove":
        Remove = input ("What do you want to remove from the lisst?\nAnswer: ").lower()
        To_Do_list.remove(Remove)
        return Remove

while True:
    for item in To_Do_list:
        print (f"To Do list:"(item["task"])) #Help with syntax by AI
    Add_Remove = input ("do you want to add or remove something from your To-Do list?\nAnswer: ").lower()
    Edit_list(Add_Remove)
    Stop_loop = input ("do you want to remove or add something else?").lower()

    if Stop_loop == "no":
        break
