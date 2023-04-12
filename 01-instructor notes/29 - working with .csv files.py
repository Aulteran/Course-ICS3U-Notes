################ WORKING WITH .CSV FILES #########

import csv       #we must always import

#file = open ("Stars.csv","r")           #creates file called Stars
#newRecord = "Brian,73,Taurus\n"
#file.write(str(newRecord))              #add new newRecord
#file.close()



file = open ("Stars.csv", "a")          # open Stars file
name = input ("Enter name:  ")          # user input
age = input ("Enter age:   ")
star = input ("Enter star sign:  ")
newRecord = name + "," + age + "," + star + "\n"
file.write(str(newRecord))              #append new info
file.close()

file = open ("Stars.csv","r")

for row in file:
    print(row)


file = open ("Stars.csv","r")
#returns a reader object that will iterate over lines in a csv file
reader = csv.reader(file)           
rows = list (reader)
print (rows[1])             #only displays row 1

file = open ("Stars.csv", "r")
search = input ("Enter the data you are searching for:  ")  #ask user for searched data
reader = csv.reader (file)
for row in file:
    if search in str(row):          #dislpays ALL rows that contain that data         
        print (row)                 #anywhere in the row
    



