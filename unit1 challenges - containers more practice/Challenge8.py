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
