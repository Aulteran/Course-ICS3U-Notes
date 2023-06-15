'''
Author: Aadil Hussain
Python Version: 3.10.4
'''
# instructions here

# You are going to make an on-screen version of the board game “Mastermind”. The
# computer will automatically generate four colours from a list of possible colours (it should

# be possible for the computer to randomly select the same colour more than once). For
# instance, the computer may choose “red”, “blue”, “red”, “green”. This sequence should not
# be displayed to the user.

# After this is done the user should enter their choice of four colours from the same list the
# computer used. For instance, they may choose “pink”, “blue”, “yellow” and “red”

# After the user has made their selection, the program should display how many colours they
# got right in the correct position and how many colours they got right but in the wrong
# position. In the example above, it should display the message “Correct colour in the correct
# place: 1” and “Correct colour but in the wrong place: 1”.

# The user continues guessing until they correctly enter the four colours in the order they
# should be in. At the end of the game it should display a suitable message and tell them how
# many guesses they took.

import random

# all allowed colors :\
colors = ["red", "blue", "green", "yellow", "pink", "orange"]

# gen random colors
sequence = random.choices(colors, k=4)

def check_guess(guess):
    correct_color_position = 0
    correct_color_wrong_position = 0

    for i in range(4):
        if guess[i] == sequence[i]:
            correct_color_position += 1
        elif guess[i] in sequence:
            correct_color_wrong_position += 1

    return correct_color_position, correct_color_wrong_position

# main loop/global loop whatev u wanna call it ig
guesses = 0
while True:
    guesses += 1

    # get the end user guess
    user_guess = []
    for i in range(4):
        color = input(f"Enter color {i + 1}: ")
        user_guess.append(color)

    # checking the guess
    correct_position, wrong_position = check_guess(user_guess)
    print(f"Correct color in the correct place: {correct_position}")
    print(f"Correct color but in the wrong place: {wrong_position}")

    # check if user guessed correct
    if correct_position == 4:
        print(f"Congratulations! You guessed the correct sequence in {guesses} guesses.")
        break
