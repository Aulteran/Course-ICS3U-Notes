# Challenge 4
# Write a program with two functions. The first function should take an 
# integer as a parameter
# and return the result of the integer divided by 2. The second function should 
# take an integer
# as a parameter and return the result of the integer multiplied by 4. Call the 
# first function, save
# the result as a variable, and pass it as a parameter to the second function.

def func1(num):
    return '''
    The number divided by 2 is
    ---------[%i]---------'''%num/2

def func2(num):
    return '''
    The number times 4 is
    -------[%i]--------'''%num*4

var = func1(2)

func2(var)
