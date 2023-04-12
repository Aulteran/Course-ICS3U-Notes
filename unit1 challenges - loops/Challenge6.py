# Challenge 6
# Ask the user to input a number and then ask if they want to double the 
# number. If they answer “y” multiply the number by 2 and display the answer.
# Keep repeating this loop, doubling their number each time, until they no 
# longer reply “y”.

doublingNum = int(input("enter a number: "))
doubleQuery = input("do you want to double this num?[y/n]: ").lower()

while doubleQuery == "y":
    doublingNum *= 2
    print(doublingNum)
    doubleQuery = input("do you want to double this num?[y/n]: ").lower()