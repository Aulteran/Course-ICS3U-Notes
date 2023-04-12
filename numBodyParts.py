#write code to count num of heads, shoulders, knees, and toes at a party.
#there are 4 ppl at the party
people = 4

#body parts per person
numOfHeadsPerBody = 1
numOfShouldersPerBody = 2
numOfKneesPerBody = 2
numOfToesPerBody = 10

NumHeads = numOfHeadsPerBody * people
NumShoulders = numOfShouldersPerBody * people
NumKnees = numOfKneesPerBody * people
NumToes = numOfToesPerBody * people

print("------------[Assignment 1]------------")
print("Number of Heads: %i\nNumber of Shoulders: %i\nNumber of Knees: %i\nNumber of Toes: %i\n" %(NumHeads, NumShoulders, NumKnees, NumToes))
print("Total Body Parts at Party: " + str(NumHeads + NumShoulders + NumKnees + NumToes))
print("--------------------------------------")