'''

# WHILE Loops
timeLeft = 5

while timeLeft > 0:
    print(timeLeft)
    timeLeft -= 1 #decrementation

# use a while loop to count from 1 to 10
# after that, print 'BLASTOFF'

count = 1

while count<10:
    print(count)
    count-=1
print("BLASTOFF")

# FOR Loops
# to loop through a range of numbers
for i in range(2, 30): #(startValue, endValue)
    print(i)
    # (endValue is not inclusive)

# to loop through at a set interval
for i in range(0,100,5): #(startValue, endValue, skipValue)
    print(i)

'''

# paractise:
num = int(input("enter a numba: "))

while num < 10 or num > 20:
    num = int(input("enter a numba: "))
print("You have chosen a number in range.")