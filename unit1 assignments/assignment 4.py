try:
    age = input("enter your age: ")

    if age >= 18:
        print("You can vote")
    elif age <= 17 and age >= 0:
        print("Too young to vote")
    elif age < 0:
        print("You are a time traveler")
    else:
        print("Error.")
except(ValueError):
    print("Invalid Input")