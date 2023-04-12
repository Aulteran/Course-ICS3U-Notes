# Create a list of four three-digit numbers. Display the list to the user, 
# showing each item from the list on a separate line. Ask the user to enter a 
# three digit number. If the number they have typed in matches one in the 
# list, display the position of that number in the list, otherwise display the 
# message ‘that is not in the list.’

threeDigitnums = [123, 456, 789, 999]

print(threeDigitnums)

checknum = int(input("enter a three digit num: "))

for i in threeDigitnums:
    if checknum == i:
        isIn = True
        break
    else:
        isIn = False

if isIn == True:
    print("indexed at: ", threeDigitnums.index(checknum))
elif isIn == False:
    print("that is not in the list")