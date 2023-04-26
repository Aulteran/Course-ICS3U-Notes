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