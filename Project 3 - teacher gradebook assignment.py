'''
Project: Teacher Gradebook Assignment
Author: Aadil Hussain
Python Version: v3.10.11 64-bi
'''

# Mr. Petrella is looking to create a program to help him tabulate
# the marks of an assignment that he has
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
# University - Must have two assignments

import statistics

gradebook = {}

assign1_grades_list = []
assign2_grades_list = []

try:
    num_students = int(input("how many students in gradebook: "))
    assign1val = int(input('value for assignment 1: '))
    assign2val = int(input('value for assignment 2: '))
except ValueError:
    print("invalid input, restart")

for i in range(1, num_students+1):
    try:
        gradebook[input(f"Name for student{i}: ")] = {'Assign1': {}, 'Assign2': {}}
    except ValueError:
        print("invalid input")


for item in gradebook.items():
    print(f"Current Student: {item[0]}")
    item[1]['Assign1']['Mark'] = int(input("Mark for assignment 1: "))
    item[1]['Assign2']['Mark'] = int(input("Mark for assignment 2: "))
    item[1]['Assign1']['Percent Grade'] = (item[1]['Assign1']['Mark'] / assign1val) * 100
    item[1]['Assign2']['Percent Grade'] = (item[1]['Assign2']['Mark'] / assign2val) * 100
    assign1_grades_list.append(item[1]['Assign1']['Percent Grade'])
    assign2_grades_list.append(item[1]['Assign2']['Percent Grade'])
while True:
    do_sum = int(input("===GRADEBOOK===\n1. View Class Stats\n2. View Student\n3. Exit\nSelect: "))
    if do_sum == 1:
        print('Class Assign1 Mean: ', statistics.mean(assign1_grades_list))
        print('Class Assign1 Mode: ', statistics.mode(assign1_grades_list))
        print('Class Assign1 Median: ', statistics.median(assign1_grades_list))
        print('Class Assign2 Mean: ', statistics.mean(assign2_grades_list))
        print('Class Assign2 Mode: ', statistics.mode(assign2_grades_list))
        print('Class Assign2 Median: ', statistics.median(assign2_grades_list))
    elif do_sum == 2:
        lookup = input("Student to lookup: ")
        assignlookup = input("assignment to lookup[Assign1/Assign2]: ")
        print('Mark for Student: ', gradebook[lookup][assignlookup]['Mark'])
        print('Grade for Student: ', gradebook[lookup][assignlookup]['Percent Grade'], '%')
    elif do_sum == 3:
        break
    else:
        print('Invalid Input')

print("baibai, pls gimme good grade\np.s. was 1am making this, might be bad")
