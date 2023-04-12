###############GLOBAL VS. LOCAL VARIABLES#################

#THESE ARE GLOBAL VARIABLES BECAUSE THEY WERE NOT DEFINED WITHIN A FUNCTION

x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()

###################################################

#THESE VARIABLES ARE DEFINED WITHIN A FUNCTION SO THEY CAN'T BE CALLED
#OUTSIDE OF THE FUNCTION ITSELF


def f():
    x = 1
    y = 2
    z = 3


print(x)
print(y)
print(z)

####################################


#WHAT IF WE TRY TO CALL IT??? (UNCOMMENT BELOW TO SEE ERROR)

#def f():
    #a = 1
    #b = 2
    #c = 3


#print(a)
#print(b)
#print(c)

########################################


#You can write to a global variable from anywhere, but writing to a global
#variable inside of a local scope takes an extra step.
#You must explicitly use the global keyword, followed by the variable you want to change.

hundo = 100

def f():
    global hundo
    hundo += 1          #This is called an increment, also you can decrement
    print(hundo)

f()

def decrement():
    global hundo
    hundo -= 10         #This is a decrement
    print (hundo)

decrement()



