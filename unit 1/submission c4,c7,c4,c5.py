'''
ICS 3U

Challenges - Math # 4,7

Challenges Functions #4,5
'''

# Math Challenge 4
# A parcel is thrown downward at a speed of v m/s from an airplane at 
# altitude 11000 m. As it falls, its distance from the ground is given by the 
# formula -4.9t2 – vt + 11000, where t is the time in seconds since it was 
# dropped. Write a program to output the time it will take to reach the ground.
# The input to your program is the positive floating-point number v. The 
# required time is given by the quadratic formula:

import math

speed = float(input("enter the speed(m/s): "))

v = speed
t = ((v - math.sqrt(v**2 - (4 * -4.9 *1100)))/(2*-4.9))

print("time: %f seconds" %t)


# Math Challenge 7
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
            

# Functions Challenge 4
# Write a program with two functions. The first function should take an 
# integer as a parameter
# and return the result of the integer divided by 2. The second function should 
# take an integer
# as a parameter and return the result of the integer multiplied by 4. Call the 
# first function, save
# the result as a variable, and pass it as a parameter to the second function.

def func1(num):
    return '''
    The number divided by 2 is
    ---------[%i]---------'''%num/2

def func2(num):
    return '''
    The number times 4 is
    -------[%i]--------'''%num*4

var = func1(2)

func2(var)


# Functions Challenge 5
# Write a function that converts a string to a float and returns the result. Use
# exception
# handling to catch the exception that could occur.

def strtofloat(string):
    try:
        return float(string)
    except(ValueError):
        print('''
        This is an invalid input,
        Please restart the program and try again.''')
