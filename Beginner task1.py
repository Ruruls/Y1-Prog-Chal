print ("What is your name?")
# We take the users input here and use it to put it into a variable, then say it back to the user
firstname = input()
print ("Hello,",firstname)

print("What is your surname?")
surname = input()
#We are taking the users 2nd input and making it a value
print ("Your surname is,",surname)

print ("Hello,",firstname,surname)
# Combine the 2 variables.
print("Your initials are:",firstname[0],surname[0])
#Take the first letters of both variables.
fullname = firstname + surname
print ("Your fullname is,",fullname)
#Combine the 2 variables into 1 print. 
print(surname.upper(),firstname)
#.upper makes surname uppercase. Len takes the amount of letters from each name
letter = len(firstname)
letter2 = len(surname)
#letter is first names letters, letter 2 is surnames letters.
print("The amount of letters in your firstname is ",letter)

print("What is your username? Hint is: 3 letters of surname, 1 of 1st name and length of your surname")      
usernameguess = input()
#Username combines the first 3 surname letters, the amount of letters and first letter of first name 
username = surname[0], surname[1], surname[2], firstname[0], letter2
#We are waiting until this value is the same as username. If not give more attempts 
if usernameguess == username:     
    print("Correct Username")
else:
    print("Incorrect")
while username != username: 
    print("Please attempt again")
    usernameguess = input()
#User has unlimited attempts to guess the password. 






