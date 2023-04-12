# Challenge 1
# Egg cartons each hold exactly 12 eggs. Write a program which reads an 
# integer number of eggs from input, then prints out two numbers: how many 
# cartons can be filled by these eggs, and how many eggs will be left over.

carton  = 12

try:
    numEggs = int(input("number of eggs: "))
except(ValueError):
    print("invalid input")

print("full cartons: %i" %(numEggs/carton))
print("remaining eggs: %i" %(numEggs%carton))