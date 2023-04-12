# Ask the user to enter two numbers. Find out which number if larger and then then display how 
# many times the smaller number goes into the larger number (use a whole number division for this). 

num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

smolNum = min(num1, num2)
bigNum = max(num1, num2)

print(bigNum//smolNum)