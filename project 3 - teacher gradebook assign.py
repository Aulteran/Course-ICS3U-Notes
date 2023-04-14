# Mr. Petrella is looking to create a program to help him tabulate the marks of an assignment that he has 
# marked. He comes to you looking for help. In this assignment you must have the following criteria:
# 1) Ask the total number of students
# 2) Ask the Total Assignment Value (what is it out of?) ie. 10
# 3) Ask the mark the student received (For each student) ie. 6
# 4) Calculate the percentage for each student (using step 2 & 3) ie. 60%
# 5) Store the averages in a container
# 6) Display the results of the class
# 7) Have the program calculate the mean, median, and mode of the entire class
# University LEVEL ADD-ON:
# 8) Have the program able to call and display a student grade’s by inputting their name

import statistics

gradebook = {}

all_grades_list = []
try:
    num_students = int(input("how many students in gradebook: "))
    assign_val = int(input('what is the assigment out of: '))
except(ValueError):
    print("invalid input, restart")

for i in range(1, num_students+1):
    try:
        gradebook[input(f"Name for student{i}: ")]['Mark'] = int(input(f"Mark for student{i}: "))
    except(ValueError):
        print("invalid input")

for student in gradebook:
    gradebook[student]['Percent Grade'] = (gradebook[student]['Mark'] / assign_val) * 100
    all_grades_list.append(gradebook[student]['Percent Grade'])

while True:
    do_sum = int(input("===GRADEBOOK===\n1. View Class Stats\n2. View Student\n3. Exit\nSelect: "))
    if do_sum == 1:
        print('Class Mean: ', statistics.mean(all_grades_list))
        print('Class Mode: ', statistics.mode(all_grades_list))
        print('Class Median: ', statistics.median(all_grades_list))
    elif do_sum == 2:
        lookup = input("Student to lookup: ")
        print('Mark for Student: ', gradebook[lookup]['Mark'])
        print('Grade for Student: ', gradebook[lookup]['Percent Grade'])
    elif do_sum == 3:
        break
    else:
        print('Invalid Input')
