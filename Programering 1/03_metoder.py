import time

num = 0
def Hello32(num):
    while True:
        if num < 31:
            print ("Hello")
            num +=1
            return num

def kvadrat():
    tal = int(input ("skriv ett tal du vill veta kvadraten av\nSvar:"))
    kvadraten = tal ** 2
    print (f"kvadraten ur {tal} är {kvadraten}")
    return kvadraten

def Multi():
    x = float(input ("skriv ett tal\nSvar:"))
    y = float(input ("skriv ett till tal\nSvar:"))
    float_svar = x * y

    print (float_svar)
    return float_svar, x, y

def RightTriangleArea():
    x = float(input("skriv ett tal\nSvar:"))
    y = float(input("Skriv ett til tall\nSvar:"))

    AreaTriangle = x * y / 2
    print (AreaTriangle)
    return AreaTriangle, x, y

def CircleArea():
    x = float(input("skriv hur långt det är från mitten til kanten av cirkeln\nSvar:"))
    
    RadieGångerTvå = x * x / 3.14 
    print (RadieGångerTvå)
    return RadieGångerTvå, x

def Get_Number_Input():
    while True:
        try:
            x = int(input ("skriv ett tal: "))
            time.sleep(1)
            print (f"ditt tal du skrev är {x}")
            break
        except ValueError:
            time.sleep(1)
            print ("skriv bara tal")

def Get_Choice():
    Get_Choice_Array = [

    ]
    num = 0
    x = 0
    while num < 3:
        s = input ("skriv in ett ord eller mening: ")
        Get_Choice_Array.append(s)
        num +=1
    while x < 3:
        print (f"{Get_Choice_Array[x]}")
        x +=1
    choose = input ("choose one of these 3 by typing 1, 2 or 3: ")


Get_Choice()