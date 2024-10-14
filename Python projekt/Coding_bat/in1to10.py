# if n is in range 1 to 10 then return true
# if n is less than 1 or more than 10 and outside_mode is true then return true but if outside_mode is false then return false 

n = int(input ("say a number: "))
outside_mode = input ("what is outside mode ").lower()
def in1to10():
    if n < 1 or n > 10 and outside_mode == "true":
        return ("True")
    elif n < 1 or n > 10 and outside_mode == "false":
        return ("False")
    elif n in range (1, 10):
        return ("True")
    
s = in1to10()
print (s)