# Challenge 4
# Alter the previous program to ask the user for a starting number and an 
# ending number. Display all the numbers in that range (including both the 
# starting and ending numbers they entered).

startNum = int(input("enter a starting number: "))
endNum = int(input("enter an ending number: ")) + 1

for i in range(startNum, endNum):
    print(i)