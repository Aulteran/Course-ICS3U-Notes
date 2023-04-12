# Ask how many people the user wants to invite to a party. If they enter a number below 10, ask 
# for the names and after each name display “[name] has been invited”. If they enter a number which
# is 10 or higher, display the message “Too many people”. 

def getInt(prompt):
    try:
        return int(input((prompt, ": ")))
    except(ValueError):
        print("invalid input")

guests = getInt("how many people will you invite to the party?")

if guests < 10:
    print("what are their names?")
    for i in range(guests+1):
        name = input("guest ", i)
        print(name, " has been invited.")
elif guests >= 10:
    print("Too many people")