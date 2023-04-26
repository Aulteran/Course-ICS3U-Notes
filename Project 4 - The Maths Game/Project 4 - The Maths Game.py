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
