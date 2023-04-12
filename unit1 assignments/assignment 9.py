# Display the following message: 
# If the user enters 1, it should ask them for the length of one of its sides and display the area. If they 
# select 2, it should ask for the base and height of the triangle and display the area. If they type in 
# anything else, it should keep repeating the question until they enter either a 1 or a 2. 

def getInt(prompt):
    try:
        return int(input((prompt, ": ")))
    except(ValueError):
        print("invalid input")

userIn = getInt("enter 1 or 2")

while userIn < 1 or userIn > 2:
    userIn = getInt("enter 1 or 2")

if userIn == 1:
    len = getInt("what is the length of one of its sides?")
    area = len ** 2
    print("The area is ", area)
elif userIn == 2:
    base = getInt("what is the base of the triangle?")
    height = getInt("what is the height of the triangle?")
    area = (base*height)/2
    print("The area is ", area)