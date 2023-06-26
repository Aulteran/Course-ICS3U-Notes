'''
Author: Aadil Hussain
Python Version: 3.11.4
'''

import time

SALES_ITEMS = ['iPad', 'Macbook', 'iPhone', 'Samsung']
ITEM_PRICES = {'iPad': 519.00, 'Macbook': 1050.50, "iPhone": 799.55, "Samsung": 699.23}

MENU = f'''
====Sales Tax Calc====
Welcome to STCv10.2
Here are the items:
1) {SALES_ITEMS[0]}
2) {SALES_ITEMS[1]}
3) {SALES_ITEMS[2]}
4) {SALES_ITEMS[3]}
5) Exit Program
Make Selection: '''

def getint(prompt):
    '''gets int input from user without error'''
    try:
        return int(input(prompt))
    except ValueError:
        print("invalid input")

def is_student():
    while True:
        resp = input("\nDo you have a student card?[Y/N]: ").lower()
        if resp[0] == 'y':
            return True
        elif resp[0] == 'n':
            return False
        else:
            print("invalid option")

def calcTax(item, studentcard: bool):
    # Determine pretax price
    if studentcard:
        price = 0.85*ITEM_PRICES[item]
    else:
        price = ITEM_PRICES[item]
    print(f"\n{item}: {price}")
    # Determine Tax
    tax = 0.13*price
    print(f"Sales Tax: {round(tax, 2)}")
    # Show total
    total_cost = price + tax
    print(f"Total Cost: {round(total_cost, 2)}")
    time.sleep(3)

while True:
    selection = getint(MENU)
    if selection == 5:
        break
    if selection >= 1 and selection <= 4:
        selecteditem = SALES_ITEMS[selection-1]
    else:
        print("Invalid Option")
        continue
    student = is_student()

    calcTax(selecteditem, student)

print("goodbye! pls gimme a 100 lols")
