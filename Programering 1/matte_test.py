#frågar frågan x*6 = 42
#skriver användaren något som inte är siffra ska programmet behandla det
#skriver användaren fel svar ska koden behandla det
#användaren ska veta om deras svar för högt eller lågt

do_again = True
answer = 7
while do_again:
    question = int(input ("what is x in the equation x * 6 = 42"))
    while True:
        try:
            question = int(input("What is x in the equation x * 6 = 42? "))
            break  # Exit the loop if the input is a valid integer
        except ValueError:
            print("You can only input numbers. Please try again.")

    if question == answer:
        print ("you are right")
        do_again = False
    elif question > answer:
        print ("your guess is too high")
    elif question < answer:
        print ("your guess is too low")


