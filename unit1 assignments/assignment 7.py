# Write a program to help you feed your friends at a party by doing some math about square pizzas. Add
# an input so the user can input for sidelength L of the pizza in cm. The area of the pizza should be 
# computed using the formula A = L * L. Then, assuming that each person needs to eat 100 cm2 of pizza, 
# compute the number of people it can feed, rounded down to the nearest integer. Hint: ex. If inputStr is 
# 17.5”, the area will be 306.25 cm2, so 3 is the correct output. 

import math

pizzaSideLen = float(input("What is the sizelength of the pizza(in cm, pls)?: "))
print(":)")

#calculates the area of the pizza
pizzaArea = pizzaSideLen*pizzaSideLen

#finds amt of (fullybodied)ppl tht can eat za pizza
pplThtCanEat = math.floor(pizzaArea/100)

print(pplThtCanEat, 'ppls tht can eat za pizzaa')