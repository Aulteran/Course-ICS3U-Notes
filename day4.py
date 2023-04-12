'''
#warmup

userIn = input("pick a food: ").lower()

if userIn == "pizza":
    print("i love pizza.")
elif userIn == "turkey":
    print("only a slice of Turkey would make Hungary full.")
else:
    print("what you dont like my food?")
'''

# Exception Handling

try:
    a = int(input("type a num: "))
    b = int(input("type a num: "))
    
    print(a/b)
except(ZeroDivisionError):
    print("Invalid Input.")

'''
for specfic errors,
except(error):
for all errors to be excepted,
except:
'''