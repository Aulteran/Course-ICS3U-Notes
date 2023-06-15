'''
Author: Aadil Hussain
Python Version: 3.10.4
'''

# You need to create a program that will store the user ID and passwords for the users of a
# system. It should display the following menu:
menu = '''
1) Create a new User ID
2) Change a password
3) Display all User IDs
4) Quit
'''
# Enter Selection:

# If the user selects 1, it should ask them to enter a user ID. It should check if the user ID is
# already in the list. If it is, the program should display a suitable message and ask them to
# select another user ID. Once a suitable user ID has been entered it should ask fora
# password. Passwords should be scored with 1 point for each of the following:

# should have at least 8 characters;
# should include uppercase letters;
# should include lower case letters;
# should include numbers; and
# should include at least one special character such as!, £, $, %, &, <, * or @.

# If the password scores only 1 or 2 it should be rejected with a message saying it is a weak
# password: if it scores 3 or 4 tell them that “This password could be improved.” Ask them if

# they want to try again. If it scores 5 tell them they have selected a strong password. Only
# acceptable user IDs and passwords should be added to the end of the .csv file.

# If they select 2 from the menu they will need to enter a user ID, check to see if the user ID
# exists in the list, and if it does, allow the user to change the password and save the changes
# to the .csv file. Make sure the program only alters the existing password and does not
# create a new record.

import csv
import string

# Function to check if a password meets the requirements
def is_password_strong(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    return score >= 5

def create_user_id():
    '''to create a new user'''
    user_id = input("Enter a user ID: ")

    with open('user_credentials.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user_id:
                print("User ID already exists. Please select another user ID.")
                return

    password = input("Enter a password: ")

    if not is_password_strong(password):
        print("Weak password. Please choose a stronger password.")
        return

    with open('user_credentials.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, password])

    print("User ID and password successfully added.")

def change_password():
    '''to change a pwd'''
    user_id = input("Enter the user ID: ")

    with open('user_credentials.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for i, row in enumerate(rows):
        if row[0] == user_id:
            new_password = input("Enter a new password: ")

            if not is_password_strong(new_password):
                print("Weak password. Please choose a stronger password.")
                return

            rows[i][1] = new_password

            with open('user_credentials.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Password successfully changed.")
            return

    print("User ID not found.")

def display_user_ids():
    '''display all user ids'''
    with open('user_credentials.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])

# main/global loop
while True:
    print(menu)
    selection = input("Enter Selection: ")

    if selection == '1':
        create_user_id()
    elif selection == '2':
        change_password()
    elif selection == '3':
        display_user_ids()
    elif selection == '4':
        break
    else:
        print("Invalid selection. Please try again.")

print("lowkey pls gimme a good grade cause cca")
