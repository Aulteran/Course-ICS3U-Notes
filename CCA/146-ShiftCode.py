'''
Author: Aadil Hussain
Python Version: 3.10.4
'''

# A shift code is where a message can be easily encoded and is one of the simplest codes to use.
# Each letter is moved forwards through the alphabet a set number of letter
# represented by a new letter.
# For instance, "abc" becomes "bcd" when the code is shifted by one

# You will need to create a program which wil display the following menu:
menu = '''
Welcome to ShiftCode v10.2
1) Make a code
2) Decode a message
3) Quit
Make Selection: '''

# Both cases will be allowed
# Punctuation will not be allowed

# will convert msg to unicode char IDs so i can jus subtract 1 from it and boom
# update: doesnt work for Z
# update 2: lol i couldve just used modulo
# update 3: boom shakalaka its doneee

def get_num(prompt):
    '''returns a number input'''
    try:
        return int(input(prompt))
    except ValueError:
        print("invalid input")

def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

def decode_message(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message

while True:
    user_selection = get_num(menu)

    if user_selection == 1: # Make a code
        code_msg = input("Enter the string to encode: ")
        shift = get_num("Enter an encoding number: ")
        print(encode_message(code_msg, shift))
    elif user_selection == 2: # Decode a message
        coded_msg = input("Enter the string to decode: ")
        shift = get_num("Enter the encoding number: ")
        print(decode_message(coded_msg, shift))
    elif user_selection == 3: # Quit
        break
    else:
        print("invalid selection")

print("Thank you for using ShiftCode v10.2")
