#############THINGS TO DO WITH LISTS####################3

my_list = [
    "raptors",
    "clippers",
    "lakers",
    "rockets",
    "nuggets",
    "bucks",
    "magic",
    "jazz",
    "celtics",
    ]

################################

print (my_list)

print (my_list[0])              #indexing

print (my_list[-1])             #negative indexing

print (my_list[2:5])            #range from list [start:end]

my_list[1] = "knicks"           #changes an item in the list

print (my_list)

print(len(my_list))             #print length of list

my_list.append("nets")          #add item to list
print (my_list)

my_list.insert(0, "wizards")    #add item to specific order in list
print (my_list)

my_list.remove("magic")         #removes item by NAME
print (my_list)

del my_list[6]                  #deletes a specific item
print (my_list)



#################################


check = input("Enter a team name: ")            #check if item is in list

if check in my_list:
    print("Yes, this team is in the list of NBA teams")
else:
    print ("This team is not in the list")


#################################

input_string = input("Enter family member first names separated by comma:  ")

family_list = input_string.split(",")           #uses input to separate famiy member names
                                                #in a list


print("\n")
print("Printing all family member names")
for name in family_list:
    print(name)






