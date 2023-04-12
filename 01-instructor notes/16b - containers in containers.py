#STORING A TUPLE INSIDE OF A LIST


locations = []                  #This is a list
la = (34.0522, 188.2437)        #This is a tuple
chicago = (41.8781, 87.6298)    #This is a tuple
locations.append(la)            #Adding a Tuple into a List 'locations'
locations.append(chicago)       #Adding a Tuple into a List 'locations'
print(locations)

#################################################

eights = ["Edgar Allan Poe",        #This is a List
          "Charles Dickens"]

nines = ["Hemingway",               #This is a List
"Fitzgerald",
"Orwell"]

authors = (eights, nines)           #This is a Tuple

print(authors)

################################################

bday = {"Hemingway":                #This is a dictionary
"7.21.1899",
"Fitzgerald":
"9.24.1896"}

my_list = [bday]                    #This is a list

print(my_list)

my_tuple = (bday,)                  #This is a tuple

print (my_tuple)

################################################

ny = {"location":           #This is a dictionary
(40.7128,                   #Location is the 1st key to dictionary  
74.0059),                   #The Tuple is first key value

"celebs":                   #Celebs is the 2nd key to the dictionary
["W. Allen",                #The list the 2nd key value
"Jay Z",
"K. Bacon"],

"facts":                    #Facts are the 3rd key to the dictionary
{"state":                   #The dictionary is the 3rd key value
"NY",
"country":
"America"}

}

n = input("Choose from location, celebs, facts: ").lower()

if n in ny:
    ny = ny[n]
    print(ny)
else:
    print("Not found.")


################################################








print(my_tuple)
