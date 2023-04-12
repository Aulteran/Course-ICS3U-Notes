# warmup

def intQuery(prompt):
    try:
        return int(input(prompt))
    except(ValueError):
        print("invalid input")

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

while True:
    option = intQuery('''
        1) add
        2) subtract
        3) exit
        Select: 
        ''')
    
    if option == 1:
        print(add(intQuery("What is the first number?: "), intQuery("What is the second number to add to the first?: ")))
    elif option == 2:
        print(sub(intQuery("What is the first number?: "), intQuery("What is the second number to subtract from the first?: ")))
    elif option == 3:
        print("Exiting . . .")
        break
    else:
        print("Invalid Input")
