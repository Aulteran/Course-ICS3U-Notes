###########FLOW CHART CHALLENGE #################

ask = int(input("Please enter a number"))

while ask < 10 or ask > 20:
    print ("Your number is out of range")
    ask = int(input("Please enter a number"))
print ("You have chosen a number in range")
