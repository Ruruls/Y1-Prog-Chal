while True: 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "password": 
        print("Login successful!") 
        break 
    else: print("Invalid username or password. Please try again.")


