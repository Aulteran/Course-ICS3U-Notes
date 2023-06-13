'''
Author: Aadil Hussain
Python Version: 3.10.4
'''

# A shift code is where a message can be easily encoded and is one of the simplest codes to use.
# Each letter is moved forwards through the alphabet a set number of letter
# represented by a new letter.
# For instance, "abc" becomes "bcd" when the code is shifted by one

# You will need to create a program which wil display the following menu:
menu = '''Welcome to ShiftCode v10.2
1) Make a code
2) Decode a message
3) Quit
Make Selection: '''

# Both cases will be allowed
# Punctuation will not be allowed

import string
from itertools import cycle

LOWER_CASE = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
              'n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER_CASE = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def get_num(prompt):
    '''returns a number input'''
    try:
        return int(input(prompt))
    except ValueError:
        print("invalid input")

def cycle_next(init_val: str, cycle_list: list, cycle_amt: int):
    # find index of init in list
    index = cycle_list.index(init_val)
    # type of case processing
    uppercase = bool(cycle_list[0] == "A")
    # for loop against cycle amt
    # every time, if amt index = 'z'
    # subtract cycle amt from amt completed
    # go on and continue remaining amt at 'a'
    for i in range(0, cycle_amt):
        index += 1
        val = cycle_list[index-1]
        if val.lower() == 'z':
            remaining_cycle = cycle_amt - i
            for remaining in range(0, remaining_cycle):
                val = 'a'
                if uppercase:
                    val = "A"
                val = cycle_list[remaining]
    final_val = str(val)
    return final_val

def encode_msg(message: str, encoding: int):
    '''takes string in and encodes it'''
    # checks if punctuation in msg
    for letter in message:
        if letter in string.punctuation:
            print("Punctuation is not allowed in message")
            return

    # separate words into list items
    msg_list = message.split()

    # shuffle letters
    for word in msg_list:
        numletters = 0
        newword_list = []
        for letter in word:
            if letter in LOWER_CASE:
                letter = cycle_next(letter, LOWER_CASE, encoding)
            elif letter in UPPER_CASE:
                letter = cycle_next(letter, UPPER_CASE, encoding)
            newword_list.append(letter)
            numletters += 1
        print(newword_list)

    print(msg_list)

def decode_msg(message, encryption):
    '''decodes string input'''
    raise NotImplementedError

encode_msg('z', 3)

# while True:
#     user_selection = get_num(menu)

#     if user_selection == 1: # Make a code
#         code_msg = input("Enter the string to encode: ")
#         shift = get_num("Enter an encoding number: ")
#         print(encode_msg(code_msg, shift))
#     elif user_selection == 2: # Decode a message
#         coded_msg = input("Enter the string to decode: ")
#         shift = get_num("Enter the encoding number: ")
#         print(decode_msg(coded_msg, shift))
#     elif user_selection == 3: # Quit
#         break

# print("Thank you for using ShiftCode v10.2")
