file = open("gamerscore.csv", "r")
line = file.readline()
SearchScore = int(input("Enter Gamerscore: "))
ScoreFound = 0

 

 

while(line):
    data =line.split(",")
    if int(data[1]) <= SearchScore:
        print("Handle: ",data[0])
        ScoreFound = 1
    line=file.readline()
if ScoreFound == 0:
    print("None found")
file.close()
