# add 2 ints togheter except if the answer is between 10 to 19 then return 20
x = int(input ("say a number"))
y = int(input ("say another number"))

def sorta_sum(sum):
    if x + y in range (10, 19):
        sum = 20
    else:
        sum = x + y 
    return sum

result = sorta_sum(sum)
print (result)