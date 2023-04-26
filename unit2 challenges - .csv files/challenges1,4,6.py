''''''
# ICS 3U:
# Challenges Unit #2 - .txt - 5
# Challenges Unit #2 - .csv - 1, 4, 6

import csv

# Challenge 1
data = [["To Kill a Mockingbird", "Harper Lee", "1960"],
        ["A Brief History of Time", "Stephen Hawking", "1988"],
        ["The Great Gatsby", "F. Scott Fitzgerald", "1922"],
        ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "1985"],
        ["Pride and Prejudice", "Jane Austen", "1813"]]

booksfile = open("unit2 challenges - .csv files/books.csv", 'w')
bookswriter = csv.writer(booksfile)
bookswriter.writerow(["Book", "Author", "Year Released"])
bookswriter.writerows(data)
booksfile.close()

# Challenge 4
# Using the Books.csv file, ask the user to enter a starting year and an end
# year. Display all books released between those two years.
booksfile = open("unit2 challenges - .csv files/books.csv", 'r')
books = csv.reader(booksfile)
bookslist = []
startYear = int(input("enter a starting year: "))
endYear = int(input("enter an ending year: "))
for year in range(startYear, endYear+1):
    for row in books:
        bookslist.append(row)
    for row in bookslist:
        if row == []:
            continue
        if row[0] == 'Book':
            continue
        if row[2] == str(year):
            print(row[0])

# Challenge 6
# Import the data from the Books.csv file into a list. Display the list to the
# user. Ask them to select which row from the list they want to delete and
# remove it from the list. Ask the user which data they want to change and
# allow them to change it. Write the data back to the original .csv file,
# overwriting the existing data with the amended data.
for row in bookslist:
    if row == []:
        place = bookslist.index(row)
        bookslist.pop(place)
        continue
    if row[0] == 'Book':
        place = bookslist.index(row)
        bookslist.pop(place)
bookslist.remove([])
print(bookslist)

remove = input("enter the name of book to remove: ")

for row in bookslist:
    if row[0] == remove:
        place = bookslist.index(row)
        bookslist.pop(place)

print(bookslist)
change = input("what book title do you want to change: ")
for row in bookslist:
    if row[0] == change:
        bookslist[bookslist.index(row)][0] = input("enter new title: ")
        bookslist[bookslist.index(row)][1] = input("enter new author: ")
        bookslist[bookslist.index(row)][2] = input("enter new year: ")
print(bookslist)

# booksfilenew = open("unit2 challenges - .csv files/books.csv", 'w')
with open("unit2 challenges - .csv files/books.csv", 'w') as booksfile:
    bookswriter = csv.writer(booksfile)
    bookswriter.writerow(["Book", "Author", "Year Released"])
    bookswriter.writerows(bookslist)
    booksfile.close()
