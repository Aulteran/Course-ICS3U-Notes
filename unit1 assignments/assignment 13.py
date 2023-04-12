# Take the code from the last example – First instead of a square have it print a Descending 
# Triangle like the shape below. Also, allow the user to input the number with which to start the 
# shape.

try:
    baseLen = int(input("enter a number for triangle size: "))
except(ValueError):
    print("Please enter a number")

while baseLen > 0:
    print("1 " * baseLen)
    baseLen -= 1
    