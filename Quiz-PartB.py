'''
Author: Aadil Hussain
Python Version: 3.9.12
'''

# Quiz Part-B
# Create a database for movies, 
# where there are entries pertaining to key and value.
# The key should be the name of the movie. 
# The value should be: 
# Year Released, Director, and Gross Sales. 
# The Menu should be
menu = '''Welcome to Movie Manager!
1) New Entry
2) See Entry from Database
3) Change Entry in Database
4) Exit
Make Selection: '''

movies = {}

def get_num(prompt):
    '''prompts user for num'''
    try:
        return int(input(prompt))
    except(ValueError):
        print("invalid input")

def new_entry(movie_name, year, director, gross_sales):
    '''creates a new entry in movies db'''
    movies[movie_name] = [year, director, gross_sales]

def call_entry(movie_name):
    '''shows details for a specific movie'''
    for movie, moviedata in movies.items():
        if movie == movie_name:
            print(f"Movie Name: {movie}\nYear: {moviedata[0]}\nDirector: {moviedata[1]}\nGross Sales: {moviedata[2]}")
            return
    print("Entry not found.")

def change_entry(movie_name, new_year, new_director, new_sales):
    '''changes movie item in db'''
    for movie, moviedata in movies.items():
        if movie == movie_name:
            moviedata[0] = new_year
            moviedata[1] = new_director
            moviedata[2] = new_sales

while True:
    menu_select = get_num(menu)
    if menu_select == 1:
        name = input("what is the movie's name: ").upper()
        year = input("What year did the movie release: ")
        director = input("what is the movie's director: ").upper()
        sales = input("what is the movie's gross sales: ").upper()
        new_entry(name, year, director, sales)
        print("Entry Created.")
    elif menu_select == 2:
        name = input("What movie's details would you like to view: ").upper()
        call_entry(name)
    elif menu_select == 3:
        print("NOTE: You cannot change the name of a movie.")
        proceed_query = input("Would you like to proceed?[Y/N]: ").upper()
        if proceed_query[0] == 'N':
            continue
        name = input("Name of movie to modify: ").upper()
        year = input("New movie release year: ")
        director = input("new movie director: ").upper()
        sales = input("new movie gross sales: ").upper()
        change_entry(name, year, director, sales)
    elif menu_select == 4:
        break
    else:
        print("invalid selection.")

print("Thank You for using Movie Manager.")
