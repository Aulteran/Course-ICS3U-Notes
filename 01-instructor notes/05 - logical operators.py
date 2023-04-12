# Logical Operators Examples

# The Python keyword 'and' takes two expressions and returns True if all the expressions
# evaluate to True. If any of the expressions are False, it returns False:

print ("logical operator 'and' examples")

a = 1 == 1 and 2 == 2

print (a)

b = 1 == 2 and 2 == 2

print (b)

c = 1 ==2 and 2 == 1

print (c)

d = 1 ==1 and 10!= 3 and 4 > 2

print (d)

# The keyword 'or' takes two or more expressions and evaluates to True if any of the expressions
# evaluate to True:

print ("logical operator 'or' examples")

e = 1 == 1 or 1 == 2

print (e)

f = 1 ==2 or 2==1

print (f)

#Placing the keyword not in front of an expression will change the result of the evaluation
#to the opposite of what it would have otherwise evaluated to. If the expression would have
#evaluated to True, it will evaluate to False when preceded by not:

print ("logical operator 'not' examples")

g = not 1 == 1

print (g)

f = not 1 == 2

print (f)

