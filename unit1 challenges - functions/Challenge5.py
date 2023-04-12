# Challenge 5
# Write a function that converts a string to a float and returns the result. Use
# exception
# handling to catch the exception that could occur.

def strtofloat(string):
    try:
        return float(string)
    except(ValueError):
        print('''
        This is an invalid input,
        Please restart the program and try again.''')

