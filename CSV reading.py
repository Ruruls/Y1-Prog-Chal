file = open("gamerscore.csv", "r")
line = file.readline()
SearchName = input("Please Enter a name:  ")
found = 0

while(line):
    data = line.split(",")
    if data[0]==SearchName:
        print("Handle: ",data[0])
        print("Gamerscore: ",data[1])
        found = 1
        
    line=file.readline()
if found != 1:
    print("Name is not in database")

file.close()