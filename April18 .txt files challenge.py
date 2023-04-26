'''
Author: Aadil Hussain
Python Version: 3.10.11
'''
# A software company wished for you to databse the
# personal emails of all of its employees. Create a program that:

# Func1:
# Asks the user for their email
# Stores the email to a txt file

# Func2:
# Removes a selected email
# Resaves the new list

database = 'April18 .txt files challenge.txt'

def add_email(filepath, email_to_add):
    '''adds an email to company db'''
    file = open(filepath, 'a')
    file.write(email_to_add, '\n')
    file.close()

def remove_email(filepath, email_to_remove):
    '''del email from company db'''
    with open(filepath, 'r') as fileopen:
        file = fileopen.read()
        db_extracted = []
        for email in file:
            db_extracted.append(email)

    with open(filepath, 'w') as fileopen:
        for email in db_extracted:
            if email == email_to_remove:
                continue
            fileopen.write(email)
        fileopen.close()

menu = '''Welcome to Company Email Manager
1) Add email
2) Remove email
3) Exit
Make Selection: '''

while True:
    user_input = input(menu)
    if user_input == '1':
        email = input('Enter email to add: ')
        add_email(database, email)
    elif user_input == '2':
        email = input("Enter email to remove: ")
        remove_email(database, email)
    elif user_input == '3':
        break
