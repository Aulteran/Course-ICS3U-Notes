# Enter a list of ten colours. Ask the user for a starting number between 0 
# and 4 and an end number between 5 and 9. Display the list for those colours
# between the start and end numbers the user input.

colors = ['black', 'red', 'blue', 'green', 'yellow', 'orange', 'white', 'purple', 'pink', 'grey']

startnum = int(input("enter a starting num between 0 and 4: "))

endnum = int(input("enter an ending num between 5 and 9: "))

print(colors[startnum:endnum+1])