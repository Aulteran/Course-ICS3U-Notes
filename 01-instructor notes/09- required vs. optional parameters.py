#####REQUIRED VS. OPTIONAL PARAMETERS###########

def f(x=2):
    return x**x

print(f())

print(f(4))

#First, you call your function without passing in a parameter.
#Because the parameter is optional.
#x automatically gets 2 and the function returns 4.
#Next, you call your function and pass in 4 as a parameter.
#The function ignores the defaultvalue, x gets 4 and the function returns 256.
#You can define a function that has both required and optional parameters,
#but you must define all the required parameters before the optional ones:

def add_it (x, y=10):
    return x + y

result = add_it(2)
print (result)
