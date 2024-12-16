To_Do_list = [
    {"task": "homework", "priority": 2},
    {"task": "walk the dog", "priority": 1},
]
i = 0
i = int
def priority():
    sorting = input ("what priority do you want this to have in your list?\nAnswer: ")
    To_Do_list.append(sorting)
    return sorting
def sorting():
    print (To_Do_list)
    To_Do_list.sort(key=lambda x: x["priority"])
    print (To_Do_list)

priority()
print (To_Do_list)