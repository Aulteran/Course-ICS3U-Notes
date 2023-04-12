# Challenge 7
# Write a program that finds and prints all the multiples of a number under 
# 20.

# gets intitial user num inpt
try:
    product = int(input("enter a number to factor: "))
except(ValueError):
    print("invalid input, enter a number.")

# creates a for loop to loop through all numbers between 0 and user input
if product < 20:
    for factor1 in range(0, product+1):
        # secondary loop to get all numbers between 0 and user inpt
        for factor2 in range(0, product+1):
            # checks if both factors multiply up to user inpt
            if factor1 * factor2 == product:
                print("%i times %i equals %i" %(factor1, factor2, product))
else:
    print("That's not under 20!")