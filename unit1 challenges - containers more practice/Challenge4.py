# Create a list of six school subjects. Ask the user which of these subjects 
# they don’t like. Delete the subject they have chosen from the list before you
# display the list again

subjects = ['math', 'chem', 'physics', 'bio', 'english', 'comp sci']

subjects.remove(input((subjects, "which subject do you not like?: ")).lower())

print(subjects)