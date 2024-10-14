# 0 = sun, 1 = mon, 2 = tue ... 6 = sat in array
#boolean to show if on vacation or not
#if weekday and vacation = False alarm clock should be 7:00 and weekday and vacation = true then alarm should be 10:00

day = int(input ("what day is it? "))
vacation = input ("what is vacation (True/False)?").lower() == True

def alarm_clock():
    if day in range (1, 5):
        if not vacation:
            return ("7:00")
        else:
            return ("10:00")
    elif day == "0":
        return ("10:00")
    else:
        return ("off")
    
clock_times = alarm_clock()
print (clock_times)