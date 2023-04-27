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

import csv
import random

menu = '''1) Take the Quiz
2) View Results
3) Exit
Make Selection: '''

database = 'Project 4 - The Maths Game/mathgamedb.csv'

def init_prog_db(filepath):
    '''pull any db info into program'''
    with open(filepath, 'r') as fileopen:
        filereader = csv.reader(fileopen)
        file = {}
        for row in filereader:
            if row == []:
                continue
            file[row[0]] = []
            for item in row:
                file[row[0]].append = item
    return file

def save_prog_db(filepath, data: dict):
    '''save any db info into program'''
    with open(filepath, 'w') as fileopen:
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

def get_num(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print('invalid input')

def gen_question():
    '''generates a random math question.
    returns tuple with question and answer'''
    operators = ['+', '-', '*', '/']
    randnum1 = random.randint(0,9)
    randnum2 = random.randint(0,9)
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
        answer = randnum1 / randnum2
    else:
        print('error: operator not valid')
        quit()
    question_set.append(answer)
    
    return tuple(question_set)

def start_quiz(playername):
    '''starts quiz with player name'''
    print(f'alright, {playername} - you will have 5 questions.')
    for i in range(0,3):
        print(f"Question {i}")
        user_ans = float(input())
    raise NotImplementedError

def view_scores(filepath):
    '''get and display scores from csv db'''
    raise NotImplementedError

# while True:
#     print("Welcome to the Math Game")
#     menuselect = get_num(menu)
#     if menuselect == 1:
#         start_quiz(input('what is the player\'s name: ').capitalize())
#     elif menuselect == 2:
#         pass
#     elif menuselect == 3:
#         print("Bye Bye!")
#         break
#     else:
#         print("invalid selection")
