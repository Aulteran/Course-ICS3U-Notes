'''
Author: Aadil Hussain
Python Version: 3.9.12
'''

# You have been asked to create a databasing system for a car dealership. In their system they need 
# 1)	The ability to add cars to database once they arrive
# 2)	Remove Cars from the database once they are purchased
# 3)	Change the price on cars as they devalue
# 4)	See the entire database, and all the cars on the lot.
# Please create a program (in Python – no GUI) that allows the car dealership to work through these problems
# in the database.
# Database: 
# [ID || MAKE || MODEL || YEAR]

import csv
import time

# C:/Users/mhussain0806/OneDrive - Brant Haldimand Norfolk CDSB/Github Desktop/Course-ICS3U-Notes/txt and csv - Quiz PartB - Intsructions/
filepath = "used_cars.csv"

def numQuery(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("invalid input")

def db_resave(newwrite):
    with open(filepath, 'w') as opendb:
        dbwriter = csv.writer(opendb)
        dbwriter.writerows(newwrite)
        opendb.close()

def add_car():
    car_id = numQuery("What is the ID of the car: ")
    car_make = input("What is the make of the car: ")
    car_model = input("What is the model of the car: ")
    car_year = numQuery("What is the year of the car: ")

    car = [car_id, car_make, car_model, car_year]

    with open(filepath, 'a') as opendb:
        dbwriter = csv.writer(opendb)
        dbwriter.writerow(car)
        opendb.close()

    print(f"Car Added to Database: {car}")

def remove_car():
    car_id = numQuery("What is the ID of the car to remove: ")

    with open(filepath, 'r', encoding='utf-8-sig') as opendb:
        dbreader = csv.reader(opendb)
        dblist = list(dbreader)
        database_listed = []
        for row in dblist:
            if row == []:
                continue
            database_listed.append(row)
        for car in database_listed:
            if int(car[0]) == car_id:
                print(f"Car Found: {car}")
                database_listed.remove(car)
                opendb.close()
                db_resave(database_listed)
                print("Deleted Car")
                return
        print("Car Not Found")
        opendb.close()

def modify_car_id():
    car_id = numQuery("What is the ID of the car to change: ")
    with open(filepath, 'r', encoding='utf-8-sig') as opendb:
        dbreader = csv.reader(opendb)
        dblist = list(dbreader)
        database_listed = []
        for row in dblist:
            if row == []:
                continue
            database_listed.append(row)
        for car in database_listed:
            if int(car[0]) == car_id:
                print(f"Car Found: {car}")
                new_id = numQuery("What is the new ID: ")
                car[0] = str(new_id)
                opendb.close()
                db_resave(database_listed)
                print("Changed Car")
                return
        print("Car Not Found")
        opendb.close()

def view_db():
    with open(filepath, 'r', encoding='utf-8-sig') as fileopen:
        csvopen = list(csv.reader(fileopen))
        for row in csvopen:
            if row == []:
                continue
            print(row)

menu = '''
Welcome to CarDatabaseManager!
==MAIN MENU==
1. Add Car
2. Remove Car
3. Modify Car ID
4. View All Cars
5. Exit
Make Selection: '''

while True:
    selection = numQuery(menu)
    if selection == 1:
        add_car()
    elif selection == 2:
        remove_car()
    elif selection == 3:
        modify_car_id()
    elif selection == 4:
        view_db()
    elif selection == 5:
        break
    else:
        print("Invalid Selection")

print("Bye Bye!")
