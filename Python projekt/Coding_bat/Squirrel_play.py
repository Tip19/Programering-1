# if the temp is between 60 and 90 and summer = false then return true
# if the temp is between 60 and 100 and summer = true then return true

temp = int(input ("what is the temperature? "))
summer = input ("what is summer? ").lower()

def squirrel_play():
    if temp < 60 or temp > 90 and summer == "false":
        return ("False")
    elif temp != range(60, 100) and summer == "true":
        return ("False")
    else:
        return ("True")

end = squirrel_play()
print (end)