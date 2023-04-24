# Challenge 1
# Write a new file called “Numbers.txt”. Add five number to the document
# which are stored on the same line and only separated by a comma. Once you
# have run the program, look in the location where your program is stored, and
# you should see that the file has been created. The easiest way to view the
# contents of the new text file on a Windows system is to read it using
# Notepad.

num_txt = open('unit2 challenges - .txt files/numbers.txt', 'w')
num_txt.write('1,2,3,4,5\n')

# Challenge 2
# Create a new file called “Names.txt”. Add five names to the document,
# which are stored on separate lines. Once you have run the program, look in
# the location where your program is stored and check that the file has been
# created properly.
names_txt = open('unit2 challenges - .txt files/names.txt', 'w')
names_txt.write('John\nMary\nPaul\nGeorge\nRingo\n')
names_txt.close()

# Challenge 3
# Open the Names.txt file and display the data in Python.
names_file = open('unit2 challenges - .txt files/names.txt', 'r')
names_read = names_file.read()
names_file.close()

# Challenge 4
# Open the Names.txt file. Ask the user to input a new name. Add this to the
# end of the file and display the entire file.
new_name = input("what new name would you like to add to the list: ").capitalize()
names_file = open('unit2 challenges - .txt files/names.txt', 'a')
names_file.write(new_name + '\n')
names_file.close()
names_file = open('unit2 challenges - .txt files/names.txt', 'r')
print(names_file.read())

# Challenge 5
# Display the following menu to the user:
menu = '''1) Create a new file
2) Display the new file
3) Add a new item to the file
Make a Selection: '''
# Ask the user to enter 1, 2 or 3. If they
# select anything other than 1, 2 or 3 it
# should display a suitable error message.
# If they select 1, ask the user to enter a
# school subject and save it to a new file
# called “Subject.txt”. It should overwrite any existing file with a new file. If
# they select 2, display the contents of the “Subject.txt” file. If they select 3,
# ask the user to enter a new subject and save it to the file and then display
# the entire contents of the file. Run the program several times to test the
# options.

while True:
    try:
        choice = int(input(menu))
    except(ValueError):
        print("Please enter a valid choice.")

    if choice == 1:
        subject = input("enter subject name: ")
        subject_file = open('unit2 challenges - .txt files/subject.txt', 'w')
        subject_file.write(subject + '\n')
        subject_file.close()
    elif choice == 2:
        subject_file = open('unit2 challenges - .txt files/subject.txt', 'r')
        print(subject_file.read())
    elif choice == 3:
        subject = input("enter subject name: ")
        subject_file = open('unit2 challenges - .txt files/subject.txt', 'a')
        subject_file.write(subject + '\n')
        subject_file.close()
    else:
        print("Please enter a valid choice.")
        continue
    break

# Challenge 6
# Using the Names.txt file you created earlier, display the list of names in
# Python. Ask the user to type in one of the names and then save all the
# names except the one they entered into a new file called Names2.txt.
names_file = open('unit2 challenges - .txt files/names.txt', 'r')
names = names_file.read()
print(names)
exclude = input("enter name to exclude: ").capitalize()
names2_file = open('unit2 challenges - .txt files/names2.txt', 'w')
names = names.split('\n')
for name in names:
    if name != exclude: #idk why its not excluding, will figure out later :)
        names2_file.write(name + '\n')
names2_file.close()
