# Feb 14 2023

# Warmup
num = 10
run = True

while run == True:
    print("there are %i green bottles hanging on the wall, %i green bottle hanging on the wall, and if 1 green bottle should accidentally fall,")

    num -= 1

    

    checkSum = True
    while checkSum == True:
        try:
            grBot = int(input("how many green bottles will be hanging on the wall?(enter a number): "))
        except(ValueError):
            print("Invalid Input")

        if grBot == num:
            print("There will be %i green bottles on the wall")
            checkSum = False
        elif grBot != num:
            print("Wrong, try again. ")
    
    if num == 0:
        run == False
        
print("There are no more bottles on the wall")