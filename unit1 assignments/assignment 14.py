# The square numbers are the integers of the form K x K, eg. 9 is a square number since 3x3 = 9. 
# Write a program that reads an integer n, from input and outputs all the positive square numbers 
# less than n, one per line in increasing order. For example, if the input is 16, then the correct output 
# would be (1,4,9)

import math

try:
    roofNum = int(input("enter a number: "))
except(ValueError):
    print("invalid input")

# loops through from user inpt down to 0
while roofNum-1 > 0:
    # checks if square root of the looped num is rational 
    if math.sqrt(roofNum-1) % 1 == 0:
        print(roofNum-1)
    roofNum -= 1
