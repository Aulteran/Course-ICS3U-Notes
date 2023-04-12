# Create a tuple containing the names of five countries and display the 
# whole tuple. Ask the user to enter one of the countries that have been 
# shown to them and then display the index number (ie. Position in the list) of 
# that item in the tuple

fiveCountries = ("argentina", "india", "spain", "south korea", "switzerland")

print(fiveCountries)
aCountry = input("enter one of the countries listed for their index: ").lower()

print("index is: ", fiveCountries.index(aCountry))

# Challenge 2
# Add to the previous program to ask the user to enter a number and 
# display the country in that position

indexToCheck = int(input("enter an index number for the countries: "))

print(fiveCountries[indexToCheck])