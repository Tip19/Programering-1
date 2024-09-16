import time

corrPass = 1234
corrUser = "Max"
Username = input("Username: ")
time.sleep(1)

while True:
    try:
        Password = int(input("Password: "))
        break
    except ValueError:
        print("Password must be a number.")

if Username.lower() != corrUser or Password != corrPass:
    print("Incorrect username or password")
else:
    print("Correct username and password")
