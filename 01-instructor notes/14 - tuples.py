#############    TUPLE EXAMPLES  ###################


# You cannot add new items to a tuple or change it once you've created it.
# If you try to change an object in a tuple after you've created it,
# Python will raise an exception

# To add objects to a tuple, create one with the second syntax with each
# item you want to add, separating them with commas

rndm = ("M. Jackson", 1958, True)
print (rndm)

# Even if a tuple only has one item in it, you need to put a comma after it.
# That way, Python can differentiate it from a number surrounded by parentheses
# that denote its position in the order of operations

teach = ("Mr. Petrella's class",)
print (teach)

#you can call items in a tuple the same way as a list

best_books = ("1984", "To Kill a Mockingbird", "The Goldfinch")

print (best_books[2])
