#defining functions examples

def f(x):
    return x + 1


z = f(4)


if z == 5:
    print("z is 5")
else:
    print("z is not 5")

###################################################

z = f(5)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")



#A function might have 1 parameter, no parameters, or more than one parameter
# parameters are divided using commas

#no parameter
def f():
    return 1 + 1

result = f()
print(result)


#multiple parameters

def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)


##############################################################

#len function

len1 = len("Monty")

print (len1)

len2 = len("Python")    
    
print (len2)

