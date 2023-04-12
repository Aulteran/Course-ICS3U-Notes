# Challenge 7
# Write a program that takes and input number from a user and then 
# determines if that number is even or odd.

userIn = input("enter a number: ")

if int(userIn)%2 == 0:
    print("number is even.\n")
elif int(userIn)%2 == 1:
    print("number is odd\n")
else:
    print("number does not compute")