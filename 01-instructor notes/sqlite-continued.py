import sqlite3

def view_phonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print (x)

def add_to_phone():
    newid = int(input('Enter ID: '))
    newfname = input ('Enter first name: ')
    newsname = input ('Enter surname: ')
    newpnum = input('Enter Phone number: ')
    cursor.execute("""INSERT INTO Names (id,firstname,surname,phonenumber)
    VALUES (?,?,?,?)""",(newid,newfname,newsname,newpnum))
    db.commit()

def select_name():
    selectsurname = input ('Enter a Surname: ')
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print (x)

def delete_data():
    selectid = int(input('Enter ID: '))
    cursor.execute('DELETE FROM Names WHERE id = ?', [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print (x)
    db.commit()

with sqlite3.connect('Phonebook.db') as db:
    cursor = db.cursor()





def main():
    again = 'y'
    while again == 'y':
        print()
        print('Main Menu')
        print ()
        print('1) View phone book')
        print('2) Add to phone book')
        print('3) Search for surname')
        print('4) Delete person from phone book')
        print('5) Quit')
        print ()
        selection = int(input('Enter your selection: '))
        print ()

        if selection == 1:
            view_phonebook()
        elif selection ==2:
            add_to_phone()
        elif selection == 3:
            select_name()
        elif selection == 4:
            delete_data()
        elif selection == 5:
            again = 'n'
        else:
            print ('incorrect selection entered')

main()
db.close()