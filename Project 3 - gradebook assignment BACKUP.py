# Define the number of assignments and students
num_assignments = 2
num_students = int(input("Enter the total number of students: "))

# Get the total value of each assignment
assignment_values = []
for i in range(num_assignments):
    value = int(input(f"Enter the total value of Assignment {i+1}: "))
    assignment_values.append(value)

# Create a dictionary to store student information
students = {}

# Loop through each student and get their grades for each assignment
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    grades = []
    for j in range(num_assignments):
        grade = int(input(f"Enter the grade for Assignment {j+1}: "))
        grades.append(grade)
    students[name] = grades

# Calculate the percentage for each student and store the averages
averages = []
for name, grades in students.items():
    total_score = sum(grades)
    total_possible = sum(assignment_values)
    percentage = round((total_score / total_possible) * 100, 2)
    averages.append(percentage)
    print(f"{name}: {percentage}%")

# Calculate the mean, median, and mode of the entire class
mean = sum(averages) / len(averages)
sorted_averages = sorted(averages)
midpoint = len(sorted_averages) // 2
if len(sorted_averages) % 2 == 0:
    median = (sorted_averages[midpoint-1] + sorted_averages[midpoint]) / 2
else:
    median = sorted_averages[midpoint]
mode = max(set(sorted_averages), key=sorted_averages.count)
print(f"Mean: {mean}%")
print(f"Median: {median}%")
print(f"Mode: {mode}%")

# Get a specific student's grades and percentage by inputting their name
while True:
    name = input("Enter a student's name to see their grades and percentage (or 'quit' to exit): ")
    if name == "quit":
        break
    elif name in students:
        grades = students[name]
        total_score = sum(grades)
        total_possible = sum(assignment_values)
        percentage = round((total_score / total_possible) * 100, 2)
        print(f"{name}: {grades} ({percentage}%)")
    else:
        print("Student not found.")
