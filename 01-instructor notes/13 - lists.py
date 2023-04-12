############  LIST EXAMPLES ############

# Lists are represented with brackets.
# There are two syntaxes you can use to create a list. You can create an
# empty list with the list function:

fruit = list()
print(fruit)

# Or, with brackets:

fruit = []
print(fruit)

# You can create a list with items already in it by using the second syntax []
# and placing each item you want in the list inside the brackets,
# separated by commas:

fruit = ["Apples", "Banannas", "Orange"]
print(fruit)


# There are three items in your list: "Apple", "Orange", and "Pear".
# Lists store in order. Unless you change the order of your list, "Apple" will always be the first item,
# "Orange" the second, and "Pear" the third. "Apple" is at the beginning of the list, and
# "Pear" is at the end. Add a new item to a list using the append method:

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
print (fruit) 

#### NOTE: .append always adds items to the end of the list

###Lists can also store any data type

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print (random)

# Strings, lists and tuples are iterable.
# Each item in an iterable has an index—a number representing the item's position in the iterable.
# The first item in a list has an index of 0, not 1. In the following example, "Apple" is at index 0,
# "Orange" is at index 1, and "Pear" is at index 2:
# You can retrieve an item with its index using the syntax [list_name][[index]]:

fruit = ["Apple", "Orange", "Pear"]
print(fruit[0])
print(fruit[2])

# Lists are mutable. When a container is mutable, you can add or remove objects from the
# container. You can change an item in a list by assigning its index to a new object

colours = ["blue", "green", "yellow"]
print (colours)
colours[2] = "red"
print (colours)

# You can remove the last item from a list using the method pop:

colours = ["blue", "green", "yellow"]
print (colours)
item = colours.pop()
print (item)
print (colours)


# You can combine two lists with the addition operator:

colours1 = ["blue", "green", "yellow"]
colours2 = ["orange", "pink", "black"]
print (colours1 + colours2)

# You can check if an item is in a list with the keyword 'in':
# Use the keyword 'not' to check if something isn't in the list
# you can check the length of the list (number of items in it) using the len command

colours7 = ["blue", "green", "yellow"]
print (len(colours7))

##Put it into practice##


colors = ["purple","orange","green"]

guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")

