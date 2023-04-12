#####IMPORT RANDOM EXAMPLES #######

import random


q = input("do you want to generate a random number?(y/n):   ")
q = q.lower()


while q == 'y':          
    x = random.randint(0,14)        ##return random integer number
    print (x)
    q = input("do you want to generate a random number?(y/n):   ")
if q == 'n':
    print('okay, thanks for playing')
else:
    print('you did not enter a valid response.')
    q = input("do you want to generate a random number?(y/n):   ")



####OTHER VALUABLE RANDOM SELECTIONS####

y = random.random ()      ###returns random float pt. number between 0 and 1
y = y * 1000
print (y)

z = random.randrange(0,100,5) ###random integer (start,stop,stepcount)
print (z)                            

colour = random.choice(['red','yellow','green']) ##random choice
print (colour)

