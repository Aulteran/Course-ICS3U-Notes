'''
ICS 3U

Challenges - Containers # 4

Challenges - Containers More Practice # 4,6,8
'''

attributesOfMe = {}
# ------------------------------------------PLEASE READ THE BELOW:--------------------------------------------
# unsure if you wanted us to include challenge 3 here because it's a dependant of challenge 4. i added it in and u can comment out if need be.
'''
# Challenge 3
# Create a dictionary that contains different attributes about you: 
# height, favorite color, favorite author, etc.

attributesOfMe = {
    'height': 175,
    'favorite color': 'green',
    'favorite author': 'jk rowling'
}

for attribute in attributesOfMe:
    print ("The value of your %s is %s." % (attribute, str(attributesOfMe[attribute])))
'''

# Challenge 4
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

# Challenge More 4
# Create a list of six school subjects. Ask the user which of these subjects 
# they don’t like. Delete the subject they have chosen from the list before you
# display the list again

subjects = ['math', 'chem', 'physics', 'bio', 'english', 'comp sci']

subjects.remove(input((subjects, "which subject do you not like?: ")).lower())

print(subjects)

# Challenge More 6
# Enter a list of ten colours. Ask the user for a starting number between 0 
# and 4 and an end number between 5 and 9. Display the list for those colours
# between the start and end numbers the user input.

colors = ['black', 'red', 'blue', 'green', 'yellow', 'orange', 'white', 'purple', 'pink', 'grey']

startnum = int(input("enter a starting num between 0 and 4: "))

endnum = int(input("enter an ending num between 5 and 9: "))

print(colors[startnum:endnum+1])

# Challenge More 8
# Ask the user to enter the names of three people they want to invite to a 
# party, and store them in a list. After they have entered all three names, ask 
# them if they want to add another. If they do, allow them to add more names 
# until they answer ‘no’. When they answer ‘no’, display how many people 
# they have invited to the party.

partyInvts = []

for i in range(1, 4):
    partyInvts.append(input("what is the name of invite #%i?: "%i).lower())

while True:
    continueInv = input("do you want to add more invites?[yes/no]").lower()

    if continueInv[0] == 'y':
        partyInvts.append(input("what is the name of the person u wanna inv?: ").lower())
    elif continueInv[0] == 'n':
        print("you have invited %i people to the party"%len(partyInvts))
        break
    else:
        print("please enter either 'y' or 'n'")
