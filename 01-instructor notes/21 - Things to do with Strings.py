#########THINGS TO DO WITH STRINGS ##########

author = "Hemingway"

print(author [0])         #indexing
print(author [1])
print(author [2])
print(author [3])
print(author [4])
print(author [5])
print(author [6])
print(author [7])
print(author [-1])      #negative indexing


print(author[0:3]+author[6:9]) #range for string, #concatenation (adding strings)

print (author *3)           #string multiplication

poet = "WHITMAN"
print(poet)
print(poet.lower())         #lowercase / .upper = uppecase
print(poet.capitalize())    #first letter capital

#################### FORMATTING ##############


author2 = 'William Faulkner'        #using variables as parameters
year_born = '1897'

print("{} was born in {}.".format(author2,year_born))

print("""
if a string is more
than one line
you must use triple quotes
""")

# This is useful for user input

n1 = input("enter a noun: ")
v = input("Enter a verb:  ")
adj = input("Enter an adj:  ")
n2 = input ("Enter a noun:  ")

print ("The {}" " {} " " the {}" "{}.".format(n1,v,adj,n2))


splitter = "Hello.my.name.is.Mr.Petrella".split(".")    
print (splitter)            #will split a string into a list





#####JOINING STRINGS FROM A LIST ##########

words = ['fox',
         'jumped',
         'over',
         'the',
         'moon']

one = " ".join(words)    ### the quotes identify what is in between, try &
print(one)


q = "       Helloo      White     Space       "
q = q.strip()
print (q)

equ = "All animals are equal"
equ = equ.replace("a","@")  ##### Parameter (what to look for, what to replace)
print (equ)

######FINDING AN INDEX ##############

## returns the first occurence

"animals".index("m")

#### if you're not sure you'll find a match use exception handling

while True:

    x = input("type in a word:  ")

    try:
        y = x.index("c")
        print (y)
        
    except:
        print ("not found")
    
    if x == 'stop':
        break

####USING THE IN FUNCTION ####

x = 'cat' in 'cat in the hat'
y = 'bat' in 'cat in the hat'

print (x,y)


########printing strings in a new line #####

print("roses are red \n violets are blue \n I like coding \n how about you?")


### slicing ###

#Slicing is a way to return a new iterable from a subset of the items
# in another iterable. The syntax for slicing is
#[iterable][[start_index:end_index]].
# The start index is the index to start slicing from,
# and the end index is the index to stop slicing at.

fict = ["Tolstoy",
"Camus",
"Orwell",
"Huxley",
"Austin"]

print (fict[0:3])

###slicing a string #####

ivan = "In place of death there was light."
print(ivan[0:17])
print(ivan[17:33])

