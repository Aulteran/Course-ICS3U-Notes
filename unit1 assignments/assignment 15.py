# If a x b = n , we call a x b a factorization of n. In this exercise, write a program that takes a 
# positive integer n from input, and then outputs all factorizations of n; for example, output for n=10 
# should look like
# 1 times 10 equals 10
# 2 times 5 equals 10
# 5 times 2 equals 10
# 10 times 1 equals 10

# gets intitial user num inpt
try:
    product = int(input("enter a number to factor: "))
except(ValueError):
    print("invalid input, enter a number.")

# creates a for loop to loop through all numbers between 0 and user input
for factor1 in range(0, product+1):
    # secondary loop to get all numbers between 0 and user inpt
    for factor2 in range(0, product+1):
        # checks if both factors multiply up to user inpt
        if factor1 * factor2 == product:
            print("%i times %i equals %i" %(factor1, factor2, product))
