########### ORD and CHAR ###############


###how do these relate?

print(ord('a'), ord('b'), ord('A'), ord('B'), ord(' '))
print(chr(35), chr(43), chr(100))


#Write a program that takes a character as input (a string of length 1), which you should assume is an loer-case character;
# the output should be the next character in the alphabet. If the input is 'Z', your output should be 'A'.

letter = ord(input())
letter = letter+1

if letter <= 90:
   print(chr(letter))
elif letter >=91:
   print('A')


#Pig Latin is a nonsense language. To transform a word from English to Pig Latin,
# you move the first letter to the end and add "ay" after that. For example, monkey becomes onkeymay in Pig Latin,
# and word becomes ordway. Write a program that takes a single word as input and translates it to Pig Latin

latin = input()

print(latin[1:]+latin[0]+'ay')
