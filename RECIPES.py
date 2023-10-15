import math

recipename = str(input("Recipe Name: "))
servings = int(input("Servings: "))
ingredientlist = []
amountlist = []
unitlist = []


addingredient = input("Do you want to add an ingredient? Yes/No: ") # first prompt, reasd Yes or No 
while addingredient == ("Yes"):
    ingredient = input("Ingredient: ")       # Getting ingredients  off user 
    ingredientlist.append(ingredient)
    amount = int(input("Amount (No Units):"))   # Getting amounts off user 
    amountlist.append(amount)
    unit = input("Unit (Gram, Pound etc): ")  # getting measurement off user 
    unitlist.append(unit)
    addingredient = input("Do you want to add another ingredient?: ") # Prompt to either redo the loop of adding or move to next part.
    if addingredient == "Yes":
        print("Recipe Complete")
    elif addingredient == "No":
        break

print("Name: ",recipename)
print("Servings: ",servings)
for x, y, z in zip(ingredientlist, amountlist, unitlist):
    print(x, y, z,)
servingchange = str(input("Do you want to change the number of servings for this recipe?: "))   # Prompt to either end the program or change the amount of people it can serve.
if servingchange == ("No"):  
    print("Recipe is Complete")  # End of program 
if servingchange == ("Yes"):
    servingnum = int(input("What amount of servings do you want?: "))
    if servingnum >= servings:
        changeserving = servingnum // servings
        finalamountlist = amountlist * changeserving         ## Math lets us change the amount of recipes measurement being used 
        print("Name:",recipename)
        print("Servings:",servingnum)
        for g, h, k in zip(ingredientlist, finalamountlist, unitlist): # G H K represent the 3 in brackets using zip function which yields them
            print(g,h,k,)  # Print out final ingredient list and units 
            

