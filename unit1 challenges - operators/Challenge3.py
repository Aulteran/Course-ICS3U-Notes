# Challenge 3
# Write a program that prints a message if a variable is less than or equal to 10,
# another message if the variable is greater than 10 but less than or equal to 25, 
# and another message if the variable is greater than 25.

num = 0

if num <= 10:
    print("the number is less than or equal to 10.")
elif num <= 25:
    print("the number is less than or equal to 25.")
elif num > 25:
    print("the number is greater than 25.")
else:
    print("intError: the number is NaN")