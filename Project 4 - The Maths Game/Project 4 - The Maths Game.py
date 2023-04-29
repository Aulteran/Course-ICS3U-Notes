'''
Author: Aadil Hussain
Python Version: 3.10.11
'''
# Project 4 - THE MATHS GAME
# Create a simple maths quiz that will ask the user for their
# name and then generate 5 questions with random math questions
# for them to answer. Store their name, grade, ‘out of’, final
# percentage in a .csv file. Whenever the program is run it
# should add to the .csv file and not overwrite anything.
# ***University Level***
# Questions use ALL mathematical operations (+, - , x , /)

import csv
import random
import time
import json
import requests

menu = '''1) Take the Quiz
2) View Results
3) Open Admin Panel
4) Exit
Make Selection: '''

database = 'Project 4 - The Maths Game/mathgamedb.csv'

# Planning (READ THIS):
# i approched this a little differently than one might expect:
# i pulled all csv data into the program at the beginning, and converted it into a dict-list nest
# the dict-list nest represents marks on each quiz per playername.
# once the program is complete, the dict-list is converted into a list compatible with csv,
# then it is written to the csv file.
# all former data is maintained

# intended internal db setup:
# {
# "<NAME>": ['mark', 'outof', 'percentgrade']
# }

# intended saved db setup:
# [
# ['name', 'mark', 'outof', 'percentgrade']
# ]

def init_prog_db(filepath):
    '''pull any db info into program'''
    with open(filepath, 'r', encoding='UTF-8') as fileopen:
        filereader = csv.reader(fileopen)
        file = {} # dict of db data to return
        for row in filereader:
            if row == []: # skips over empty rows
                continue
            file[row[0]] = [] # creates list in player dict key
            for item in row:
                if item == row[0]: # to not add playername into list
                    continue
                file[row[0]].append(item) # adds playerdata into list
    return file

def save_prog_db(filepath, data: dict):
    '''save any db info into program'''
    with open(filepath, 'w', encoding='UTF-8') as fileopen:
        filewriter = csv.writer(fileopen)
        # convert all data to csv compatible list
        writelist = []
        for item in data.items():
            person = []
            person.append(item[0])
            for mark in item[1]:
                person.append(mark)
            writelist.append(person)
        # Write data to csv and save
        filewriter.writerows(writelist)
        fileopen.close()

# REPLAN:
# I realized i misinterpreted the db instructions.
# Each name only needs one quiz data, not multiple quizzes.
# I'm going to redo this using append mode.
# First: make quiz
# Next: save quiz data in list
# Last: append quiz data to file
# Can reuse init_prog_db to view scores
# Gonna keep save_prog_db for now, might use later

def get_num(prompt):
    '''query num from user'''
    try:
        return int(input(prompt))
    except ValueError:
        print('invalid input')

def save_score(filename, name, mark, outof, percent):
    '''Saves user score into db'''
    with open(filename, 'a', encoding='UTF-8') as fileopen:
        filewriter = csv.writer(fileopen)
        filewriter.writerow([name, mark, outof, percent])
        fileopen.close()

def gen_question():
    '''generates a random math question.
    returns tuple with question and answer'''
    operators = ['+', '-', '*', '/']
    randnum1 = random.randint(0,9)
    randnum2 = random.randint(1,9) # avoid ZeroDivisionError
    operator = random.choice(operators)
    question_set = []
    question_set.append(str(randnum1) + operator + str(randnum2))
    # make correct answer
    if operator == '+':
        answer = randnum1 + randnum2
    elif operator == '-':
        answer = randnum1 - randnum2
    elif operator == '*':
        answer = randnum1 * randnum2
    elif operator == '/':
        answer = round(randnum1 / randnum2, 2)
    else:
        print('error: operator not valid')
        quit()
    question_set.append(answer)

    return tuple(question_set)

def start_quiz(filename, playername):
    '''starts quiz with player name'''
    print(f'Alright, {playername} - you will have 5 questions.')
    score = 0
    for i in range(0,5):
        questionset = gen_question()
        print(f"Question {i+1}: {questionset[0]}")
        while True:
            try:
                user_ans = float(input("Answer(Round to 2 Decimals): "))
                break
            except ValueError:
                print('invalid input')
        if user_ans == float(questionset[1]):
            print(f"Correct! {playername} - you got it right on question {i+1}")
            score += 1
        else:
            print(f"Incorrect! {playername} - you got it wrong on question {i+1}")
            print(f"The correct answer was {questionset[1]}")
    print("Quiz Complete")
    print("Saving Scores. . .")
    save_score(filename, playername, score, 5, round(score/5*100, 2))
    time.sleep(2)
    print("Saved!")

def view_scores(filepath):
    '''get and display scores from csv db'''
    db = init_prog_db(filepath)
    print("\n------------------------\nScoreboard:")
    if not db: #if db dict is empty
        print("No scores found.")
        print("------------------------")
        return
    for player, playerdata in db.items():
        print(f"{player}: {playerdata[0]}/{playerdata[1]}, {playerdata[2]}%")
    print("------------------------")

# =====================================
# The following section of code below is all experimental and just messing around
# will make a password protected admin portion of the app to manage the db
# Mr.P, you can try guessing the pwd and mess around with it. let's see how it goes.
# PLANNING:
# Will make API call to my RestAPI server to respond with an authentication key
# if user password has been authenticated, then lets do it

def call_api(url, data):
    '''calls my rest-api server with user pwd'''
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        try:
            api_response = response.json()
            match_value = api_response.get('match')
            
            if match_value is not None:
                return match_value
            else:
                return None
        except json.decoder.JSONDecodeError:
            return None
    else:
        return None

def auth_admin():
    '''gets input pwd and sends it to api to check auth'''
    api_url = "https://ics3u-project4-auth.andrims.workers.dev"
    data = {"inputString": input("Enter Password. Case Sensitive. (Hint, it's the course code)\nPWD: ")}
    match_result = call_api(api_url, data)

    if match_result is not None:
        if match_result:
            print("Authentication Success")
            return True
        else:
            print("Authentication Failed")
            return False
    else:
        print("Error: Failed to call the API.")

admin_menu = '''
------------------------
Admin Panel:
1) Reset Database
2) Remove Singular Player
3) Modify Player
4) Exit AdminPanel
Make Selection: '''

def reset_db(filename):
    '''clears csv database'''
    with open(filename, 'w', encoding='UTF-8') as fileopen:
        fileopen.write("")
        fileopen.close()
    print("Database Wiped.")

def del_player(filename, rem_player):
    db = init_prog_db(filename)
    for playername in db.keys():
        if playername == rem_player:
            del db[playername]
            save_prog_db(filename, db)
            print("Player Removed")
            break

def modify_player(filename, playername):
    '''change player data'''
    print("NOTE: cannot edit playername")
    db = init_prog_db(filename)
    for player, playerdata in db.items():
        if player == playername:
            try:
                playerdata[0] = int(input("Enter new mark: "))
                playerdata[1] = int(input("Enter new outof: "))
                playerdata[2] = float(playerdata[0]/playerdata[1]*100)
            except ValueError:
                print("invalid input. redo data entry.")
            save_prog_db(filename, db)
            return
    print("Player not found.")

def admin_panel(auth):
    '''admin panel and controls if user is authenticated'''
    if auth != True:
        print("Access Denied")
        return
    global database
    while True:
        admin_select = get_num(admin_menu)
        if admin_select == 1: # Reset Database
            reset_db(database)
        elif admin_select == 2: # Remove Singlular Player
            del_player(database, input("Enter playername to delete: ").capitalize())
        elif admin_select == 3: # Modify Player
            modify_player(database, input("Enter playername to modify: ").capitalize())
        elif admin_select == 4: # Exit Admin Menu
            print("returning to main menu. . .")
            break

# =====================================
# Main Application Loop
while True:
    print("\nWelcome to the Math Game")
    menuselect = get_num(menu)
    if menuselect == 1: # Take the Quiz
        start_quiz(database, input('what is the player\'s name: ').capitalize())
    elif menuselect == 2: # View Results
        view_scores(database)
    elif menuselect == 3: # Open Admin Panel
        admin_panel(auth_admin())
    elif menuselect == 4: # Exit
        print("Bye Bye!")
        break
    else: # Not valid option
        print("invalid selection")
