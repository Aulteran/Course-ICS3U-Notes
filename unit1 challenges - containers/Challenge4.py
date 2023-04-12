# Write a program that lets the user ask your height, favorite color, or 
# favorite author, and
# returns the result from the dictionary you created in the previous challenge.

whatuwant = int(input("whatchuwant?\n1.height\n2.fav color\n3.fav author\ninput:"))

if whatuwant == 1:
    print(attributesOfMe['height'])
elif whatuwant == 2:
    print(attributesOfMe['favorite color'])
elif whatuwant == 3:
    print(attributesOfMe['favorite author'])
else:
    print("not valid broski")