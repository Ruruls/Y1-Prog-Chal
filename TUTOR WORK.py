while True: 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "password": 
        print("Login successful!") 
        LoginSuccess= 1
        break 
    else: print("Invalid username or password. Please try again.")

while LoginSuccess == 1:
    input("Enter a students Information. Starting with their Surname")
