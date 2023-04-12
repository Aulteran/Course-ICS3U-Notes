# Challenge 8
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