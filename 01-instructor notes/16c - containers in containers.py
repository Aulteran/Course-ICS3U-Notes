####Containers in Containers########

#You can store containers in other containers.
#For example, you can store lists in a list:

lists = []

rap = ["Kanye West",
"Jay Z",
"Eminem",
"Nas"]

rock = ["Bob Dylan",
"The Beatles",
"Led Zeppelin"]

djs = ["Zeds Dead",
"Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print (lists)


#In this example, lists has three indexes.
#Each index is a list: the first index is a list ofrappers,
#the second index is a list of rockers, and the third index is a list of DJs.
#You can access these lists using their corresponding index:

rap = lists[0]
print(rap)

rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print(lists)


#You can store a tuple inside a list, a list inside a tuple,
#and a dictionary inside of a list or a tuple:


