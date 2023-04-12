try:
    userInt = int(input("enter an int: "))
    if userInt == 0:
        print("Zero")
    elif userInt > 0:
        print("Positive")
    elif userInt < 0:
        print("Negative")
    else:
        print("Error")
except(ValueError):
    print("Invalid Input")