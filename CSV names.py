file = open("CSVpeople1.csv", "r")
line = file.readline()
SearchName = input("Please Enter a name:  ")
found = 0

while(line):
    data = line.split(",")
    if data[0]==SearchName:
        print("Name: ",data[0])
        print("Address: ",data[1])
        print("City: ",data[2])
        print("Phone: ",data[3])
        found = 1
        
    line=file.readline()
if found != 1:
    print("Name is not in database")

file.close()