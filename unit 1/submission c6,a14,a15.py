'''
ICS 3U:

Challenges Unit 1 (Loops) - #6

Assignments Unit 1 - #14,15
'''

# Challenge 6
# Ask the user to input a number and then ask if they want to double the 
# number. If they answer “y” multiply the number by 2 and display the answer.
# Keep repeating this loop, doubling their number each time, until they no 
# longer reply “y”.

doublingNum = int(input("enter a number: "))
doubleQuery = input("do you want to double this num?[y/n]: ").lower()

while doubleQuery == "y":
    doublingNum *= 2
    print(doublingNum)
    doubleQuery = input("do you want to double this num?[y/n]: ").lower()

# Assignment 14
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

# Assignment 15
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
