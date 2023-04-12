#######EXCEPTION HANDLING##########


a = int(input("type a number:"))
b = int(input("type another:"))

print (a/b)


#What about if zero is our numerator???
############################

#try:
#    print(a / b)
#except ZeroDivisionError:
#    print("b cannot be zero.")

###########WHAT ABOUT INVALID TYPE ERROR ie. ValueError)

try:
    a = int(input("type a number:"))
    b = int(input("type another:"))
    

    print(a / b)
except(ZeroDivisionError,ValueError):
    print("Invalid input.")
