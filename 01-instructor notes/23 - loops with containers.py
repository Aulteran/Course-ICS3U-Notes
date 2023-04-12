########## LOOPS WITH CONTAINERS ###########

### FOR LOOPS TO ITERATE THROUGH ITEMS IN A LIST

shows = ["GOT",
"Narcos",
"Vice"]

for show in shows:
    print(show)


###LOOPING THROUGH A TUPLE

coms = ("A. Development",
"Friends",
"Always Sunny")

print("\n")

for show in coms:
    
    print(show)

####LOOPING THROUGH KEYS OF A DICTIONARY###

people = {"G. Bluth II":"A. Development",
"Barney": "HIMYM",
"Dennis":"Always Sunny"
}
print ("\n")

for character in people:
    print(character)



#####USING FOR LOOP TO ADD UPPERCASE TO ALL ITEMS IN LIST ###

movie = ["social network",
         "inception",
         "dark knight",
         ]

i = 0

for show in movie:
    new = movie[i]
    new = new.upper()       ###UPPERCASE FUNCTION
    #movie[i]=new            ###SAVES CHANGE TO THE LIST
    print (new)
    i += 1
    
print (movie)       

###   OR WE CAN 'ENUMERATE'   ###

for i, show in enumerate (movie):
    new = movie[i]
    new = new.upper()
    movie [i] = new
    print (new)
    


tv = ["GOT", "Narcos",
"Vice"]

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)


############appending two lists using a loop ######

tv = ["GOT", "Narcos",
"Vice"]

coms = ["Arrested Development",
"friends",
"Always Sunny"]

all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

#####   NESTING LOOPS   ######

# The first loop iterates through every integer in list1.
# For each item in it, the second loop iterates through each integer in its own iterable,
# adds it to the integer from list1 and appends the result to the list added.
# I named the variable j in the second for-loop, because I already used the variable name i in the first loop.

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:                     #IE. 1+5 = 6 // 1 +6 = 7 // 
    for j in list2:
        added.append(i + j)

print(added)



    


    
