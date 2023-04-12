# Challenge 7
# Ask the use if they want a cup of tea. If they reply with “no” or “n” repeat 
# the question. Once the loop stops display the message “Sorry, we have run 
# out of tea”.

teaQuery = input("do you want any tea?[yes/no]: ").lower()

while teaQuery != "no" or teaQuery != "n":
    teaQuery = input("do you want any tea?[yes/no]: ").lower()

print("Sorry, we have run out of tea")