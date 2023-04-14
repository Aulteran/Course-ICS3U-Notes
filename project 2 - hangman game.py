# Author: Divyanshi Dave
# Python Version: v3.11.2 64-bit

# Import main modules
import random
import time

# Cool little intro thingy i made :)
for i in range(3):
    print("Loading game . . .")
    time.sleep(1)

print("Welcome to Hangman!")

# words can be run
word_list = ["python", "java", "ruby", "javascript", "html", "css"]

# Select random word from za woord leest
chosen_word = random.choice(word_list)

# init za main vars
guesses = ''
turns = 6

while turns > 0: # MAIN GAME LOOP
    # failed attempts go brr
    failed = 0

    # Display current completion of za word
    for letter in chosen_word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')

            failed += 1

    # Check if player guessed all letters
    if failed == 0:
        print('\nYou won!')
        break

    guess = input('\nGuess a letter: ').lower()

    guesses += guess

    # Check if guess in word
    if guess not in chosen_word:
        turns -= 1
        print(f'Wong! You have {turns} turns left.') # Accidentally used f-strings, not avail in python 3.5

        if turns == 0:
            print('You lose!')

# end main loop when user runs out of turns
