answer1 = str(input("Is it known for its neck (lower case yes or no)")) 
if answer1 == "no":
    answer2 = str(input("Is it known for its speed"))
else:
    print("Your dinosaur is brontosaurus")
if answer2 == "no":
    answer3 = str(input("Is it known for flying"))
else: 
    print("Your dinosaur is Velociraptor")
if answer3 == "no":
    answer4 = str(input("Is it known for size and small arms"))
else: 
    print("Your dinosaur is Pterodactyl")
if answer4 == "no":
    answer5 = str(input("Is it known for its neck frills"))
else: 
    print("Your dinosaur is T-rex")
if answer5 == "no":
    answer6 = str(input("Is it known for its Horns"))
else: 
    print("Your dinosaur is Dilophosaurus")
if answer6 == "no":
    answer5 = str(input("Dinosaur not found"))
else: 
    print("Your dinosaur is Triceratops")