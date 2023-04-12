birthYear = input("What is your birth year?: ")
currYear =  input("What is the current year?: ")

userAge = currYear - birthYear

if userAge > 65:
    print("enjoy retirement")
elif userAge < 65:
    print("you are %i years old" % userAge)
else:
    print("you are 65")