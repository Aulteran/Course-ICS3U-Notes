'''
Author: Aadil Hussain
Python Version: 3.11.4
'''

import time

semester_marks = {} #db scheme {coursename: coursemark}
attempts = 3

def getflt(prompt):
    '''gets float input from user without error'''
    while True:    
        try:
            return float(input(prompt))
        except ValueError:
            print("invalid input")

print("\nWelcome to Semester Average Calculator")

while attempts > 0:
    print("\nBegin entering courses")
    for i in range(4):
        coursename = input("\nenter semester course name: ")
        coursemark = getflt("enter final course mark: ")
        if coursemark<0 or coursemark>100:
            attempts-=1; attfailed = True
            print("course mark cannot be below 0 or above 100")
            print("redo course entry")
            break
        semester_marks[coursename] = coursemark
        attfailed = False
    if attfailed:
        continue
    print("\nProcessing Marks")
    time.sleep(1)
    preavg_mark = 0
    for course, mark in semester_marks.items():
        preavg_mark += mark
        print(f"{course}: {mark}")
        time.sleep(0.5)
    avg_mark = round(preavg_mark/4, 1)
    print(f"Semester Avg: {avg_mark}%")
    break

if attempts == 0:
    print("\nNo more attempts left - locked out.")

print("Thank you for using SAC. pls gimme a 100 lols")
