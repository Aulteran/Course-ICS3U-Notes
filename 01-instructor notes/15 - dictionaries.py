############## DICTIONARIES EXAMPLES #############

# Dictionaries are represented with curly brackets.
# There are two syntaxes for creating dictionaries:

my_dictionary = dict()

print (my_dictionary)

my_dictionary = {}

print (my_dictionary)

##keys and values
# The first syntax has the key separated from the value by an assignment operator,
# and the second has the key separated from the value by a colon.
# A comma must separate each key-value pair.

fruits = {"Apple":
"Red",
"Banana":
"Yellow"}
print (fruits)

# Once you've created a dictionary, you can add key-value pairs to itwith the syntax
#[dictionary_name][[key]]=[value],
# and look up a value using a key with the syntax [dictionary_name][key]:

facts = dict()
# add a value
facts["code"] = "fun"
# look up a key
print(facts["code"])
# add a value
facts["Bill"] = "Gates"
# look up a key
print(facts["Bill"])
# add a value
facts["founded"] = 1867
# look up a key
print(facts["founded"])


# Use the in keyword to check if a KEY is in a dictionary. You CANNNOT use the in keyword to
# check if a VALUE is in a dictionary:

# You can delete a key-value pair from a dictionary with the keyword del:

books = {"Dracula": "Stoker",
"1984": "Orwell",
"The Trial": "Kafka"}

del books["The Trial"]

print (books)


rhymes = {"mayer": "Daughters",
"petty": "mary jane's last dance",
"gilmour": "shine on you crazy diamond",
"dylan": "tangled up in blue",
"harrison": "my sweet lord"
}

n = input("Type an artist last name:").lower()

if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")

