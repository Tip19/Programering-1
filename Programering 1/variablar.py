import time

text_array = ["Hej", "jag", "heter", "max"]

print (text_array)

text_array.append ("Eric")
time.sleep(1)
text_array.remove ("max")

print (text_array)
time.sleep(2)

print (text_array[0] + " " + text_array[3])
