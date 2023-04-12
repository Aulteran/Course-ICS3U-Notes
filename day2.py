#logical operators

1 == 1
#will evaluate as true because 1 equals 1

2 == 5
#will evaluate as false because 2 does not equal 5

2 != 4
#will evaluate as true because 2 does not equal 4

#AND - all expressions must be true to evaluate to true
print('and expressions')

a= 1==1 and 2 == 2
print(a)

b= 1==1 and 1 == 2
print(b)

c= 1==1 and 10!=3 and 4<2
print(c)

#OR - will evaluate to true if any one of the expressions is true
print('or expressions')

d= 1==2 or 2==2
print(d)

e= 1==2 or 2==1
print(e)

#NOT - will change boolean value of any expression to it's opposite (T->F and F->T)
print('not expressions')

f= not 1==1
print(f)

g= not 1==2
print(g)

##user input

#default class for input is <str>
name=input('What is your name: ')
print('Hello', name)

num=input('Enter a number: ')
#or num=int(input('Enter a number: '))

#number is still a <str> value
num=int(num)
ans=num*3

print('your number times 3 is', ans)