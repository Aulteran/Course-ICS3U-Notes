# Challenge 5
# Ask the user to input a number. If that number is more than 10 display the
# message “Too high” and ask them to try again and input another number. 
# Keep repeating this loop until they enter a number which is less than or 
# equal to 10. 

checkNum = int(input("enter a number: "))

while checkNum > 10:
    print("Too high")
    checkNum = int(input("enter a number: "))