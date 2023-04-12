# Challenge 6
# Write a program to calculate the volume and surface area of a cylinder 
# given user input.

import math as m

def numQuery(prompt):
    try:
        return float(input(prompt))
    except(ValueError):
        print("invalid input")

radius = numQuery("what is the radius of the cylinder's top?: ")
length = numQuery("What is the length of the cylinder?: ")

area = m.pi * (radius**2)
volume = area * length

circ = 2 * m.pi * radius
surfArea = (circ * length) + (2 * area)