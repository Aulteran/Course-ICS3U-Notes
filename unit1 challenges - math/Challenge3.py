# Challenge 3
# The geometric mean of two number A and B is the number
# It is commonly used to compare aspect ratios of display screens and 
# describe the average growth rate of a population. Write a program that 
# reads two lines of positive float from input, and outputs their geometric 
# mean.

import math

float1 = float(input("enter a number: "))

float2 = float(input("enter a number: "))

mean = math.sqrt(float1*float2)

print(mean)