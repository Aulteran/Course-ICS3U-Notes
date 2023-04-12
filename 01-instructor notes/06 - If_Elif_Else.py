#If statements

home = "Canada"

if home == "Canada":
    print ("Welcome Home friend")



#you can have multiple If statements

x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")

#Each if-statement will execute its code only if its expression evaluates to True. In
#this case, the first two expressions evaluate to True, so their code executes, but the third
#expression evaluates to False, so its code does not execute.



# If and Else

ans = input('Enter your home country:  ')

if ans == "Canada":
    print ("Welcome Canada")
else:
    print ("Welcome World")

#You can use the elif keyword to create elif-statements. elif stands for else if, and
#elif-statements can be indefinitely added to an if-else statement to allow it
#to make additional decisions.

home = input("type where you're from:  ")
if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")
