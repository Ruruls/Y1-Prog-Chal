import random
number = random.randint(1,100)
print (number) 
answer = input("Guess the number") 
counter = 1
while answer != (number):
    answer = int(input("Incorrect, guess again: " ))
    counter = counter + 1 
    if answer >= number:
        print("Lower")
    if answer <= number:
        print("Higher")
print("Correct! You had",counter,"attempts.")


