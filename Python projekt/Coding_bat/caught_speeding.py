#speeding 60 =< result is 0
#speeding 61 - 80 result is 1
#speeding 81 => result is 2
# if it's your bithday you get away with 5 higher
import time

speed = int(input("How fast were the going? "))
time.sleep(1)
birthday = input ("is it their birthday? ").lower()

if speed <= 60:
    print ("0")

elif speed in range (61, 80):
    if birthday == "yes" and speed <= 85:
       print("0")
    elif birthday == "no":
        print ("1")

elif speed >= 81:
    if birthday == "yes" and speed <= 86:
         print ("0")
    elif birthday == "no":
         print ("1")
               