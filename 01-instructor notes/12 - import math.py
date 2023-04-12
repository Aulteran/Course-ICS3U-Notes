############## The Math Module #################

#Your friends have eaten their square pizzas and are now ordering a round pizza.
#Write a program to calculate the area of this circular pizza.
#The input is a float r, which represents the radius in cm.
#The output should be the area in cm2, calculated using the formula  A=pi*r2. 


import math

pizza = float(input("what is the radius of the pizza in cm? "))

area = (math.pi * pizza ** 2)

print(area)


######ROUNDING WITH INT and FLOAT#########

#The expressions a // b and int(a / b) are the same when a and b are positive.
#However, when a is negative,
#a // b uses "round towards negative infinity" and
#int(a / b) uses "round towards zero."

print((-10) // 3, int((-10) / 3)) # different
print((-12) // 2, int((-12) / 2)) # same, only because 2 divides evenly into -12



