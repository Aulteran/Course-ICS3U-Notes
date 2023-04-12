# Challenge 3
# Ask the user to input a starting number. Display that number and the next 
# three numbers after that (i.e. if they enter 4 it should display 4, 5, 6 and 7).

userNum = int(input("enter a number: "))
finalNum = userNum + 3

while userNum <= finalNum:
    print(userNum)
    userNum += 1