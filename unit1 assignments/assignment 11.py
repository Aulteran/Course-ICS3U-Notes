# Create a variable called compnum and set the value to 50. Ask the user to enter a number. 
# While their guess is not the same as the compnum value, tell them if their guess is too low or too 
# high and ask them to have another guess. If they enter the same value as compnum, display the 
# message “Well done, you took [count] attempts”.

def getInt(prompt):
    try:
        return int(input((prompt, ": ")))
    except(ValueError):
        print("invalid input")

compNum = 50

userGuess = getInt("enter a number")

incorrect = True
attempts = 0

while incorrect:
    attempts += 1
    if userGuess < compNum:
        print("too low")
    elif userGuess > compNum:
        print("too high")
    elif userGuess == compNum:
        print("Well done, you took %i attempts" % attempts)
        incorrect = False

