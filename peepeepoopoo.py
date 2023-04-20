import statistics

grades = {}
tmp_list = {}
tmp_marks = []

def num_query(prompt):
    '''gets int query from user without errors'''
    try:
        return int(input(prompt))
    except(ValueError):
        print("Value was non-integer!")

def create_assign():
    global grades; global tmp_list; global class_num

    assign_name = str(input("\nWhat is the name of the assignment you are trying to add?: "))
    assign_val = num_query('What is the assignment value?: ')

    for stud_num in range(class_num):
        stud_name = str(input("What is this student's name?: "))
        stud_grade = float(input("What is this student's mark?: "))
  
        grade = (stud_grade/assign_val)*100 #if assign_val = 0 or is undefined code will break!
        tmp_list[stud_name] = grade

    if assign_name in grades.keys(): #THIS NO WORKEY!
        print('Assignment already in list!')
    else:
        grades[assign_name] = tmp_list
        tmp_list = {}

def mark_searcher():
        global grades

        try:
            print('\nAssignment search list:')
            for assignment_names in grades:
                print(assignment_names)
            filt_1 = str(input('Enter assignment: '))

            print('\nStudent search list:')
            for student_names in grades[filt_1]:
                print(student_names)
            filt_2 = str(input('Enter student: '))

            try:
                print(filt_2+"'s grade on",filt_1,'was',grades[filt_1][filt_2])
            except(KeyError):
                print('Assignment or student not recognized!')
        except:
            print('\nEnsure there are assignments with marks first!')

def calc_stats(mode_select):
    global grades; global tmp_marks
    
    try:
        if mode_select == 'overall':
            for subject in grades:
                for student in grades[subject]:
                    tmp_marks.append(grades[subject][student])
            tmp_marks.sort(reverse=True)

            print('\nThe average grade (or mean) of the class is',statistics.mean(tmp_marks))
            print('The most reoccuring grade (or mode) of the class is',statistics.mode(tmp_marks))
            print('The median of the class is', statistics.median(tmp_marks))

        elif mode_select == 'specific':
            print('\nAssignment search list:')
            for assignment_names in grades:
                print(assignment_names)
            filt_1 = str(input('Enter assignment: '))

            for student in grades[filt_1]:
                tmp_marks.append(grades[filt_1][student])
            tmp_marks.sort(reverse=True)

            print('\nThe average grade (or mean) of',filt_1,'is',statistics.mean(tmp_marks))
            print('The most reoccuring grade (or mode) of',filt_1,'is',statistics.mode(tmp_marks))
            print('The median of',filt_1,'is',statistics.median(tmp_marks))
    except:
        print('\nEnsure there are assignments with marks first!')

    tmp_marks = []

loop = True

while loop == True:
    try:
        class_num = int(input("""\nWelcome to Teacher Gradebook!
How many students are in your class?: """))
        if class_num <= 0:
            print('Number of students cannot be negative or equal to 0!')
        elif class_num > 0:
            loop = False
    except(ValueError):
        print('Not a valid input! Try again...')

loop = True

while loop == True: 
    menu = str(input("""
1. Enter data for a new assignment
2. Display overall class results and statistics
3. Display class results and statistics of specific assignment
4. Search for a students grade
5. Exit
Enter Here (1-5): """))
    if menu == '1':
        create_assign()

    elif menu == '2':
        calc_stats('overall')

    elif menu =='3':
        calc_stats('specific')

    elif menu =='4':
        mark_searcher()

    elif menu == '5':
        quit()
    
    elif menu == 'dump':
        print("\n'grades' LIST:\n",grades)
        print('TEMPORARY LIST:\n',tmp_list)
        print('TEMP MARKS:\n',tmp_marks)
        print('ALL GRADES LIST:\n',grades)
        print(grades.keys())
        print(grades.values())

    else:
        print('Entry was not an option in list!')