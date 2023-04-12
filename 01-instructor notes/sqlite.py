import sqlite3 #allows python to use the library
with sqlite3.connect('Phonebook.db') as db:
    cursor=db.cursor()

#Create the Database
cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
    id integer PRIMARY KEY,
    firstname text,
    surname text,
    phonenumber text); """
)

#Add Entries

cursor.execute(""" INSERT INTO Names (id,firstname,surname,phonenumber)
VALUES('1', 'Simon', 'Howels', '1234 3456')""")
db.commit()


db.close()

