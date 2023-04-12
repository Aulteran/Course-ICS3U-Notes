'''
ICS 3U:

Challenges Unit 1 (Operators)  #8

Assignments Unit 1 #7,8
'''

## CHALLENGE 8
# Write a program that calculates the population of a country for the next 
# four years, assuming it starts with an initial population of 10,000 in 2020, 
# and the number of people increases by 10% each year.

initPopulation = 10000
years = 4
perYearIncrease = 0.10

def populationIncrease(init, time, rate):
    finalPopulation = init*rate*time
    return finalPopulation

print(populationIncrease(initPopulation, years, (1+perYearIncrease)))

## ASSIGNMENT 7
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


## ASSIGNMENT 8
# Ask the user to enter two numbers. Find out which number if larger and then then display how 
# many times the smaller number goes into the larger number (use a whole number division for this). 

num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

smolNum = min(num1, num2)
bigNum = max(num1, num2)

print(bigNum//smolNum)