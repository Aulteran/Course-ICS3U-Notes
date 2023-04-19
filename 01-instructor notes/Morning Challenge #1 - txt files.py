# MORNING CHALLENGE:
print ('''
Today's morning challenge:
Create a program with the following menu:
1) Enter Score
2) Look at List of Scores
3) Exit
When a Score is entered, it must add it to the existing file - store and call the scores from a .txt file''')

# SOLN

def enter_score(top_five):


    file = open('store_score.txt','r')
    exist_list = file.read()
    exist_list = exist_list.split('\n')
    exist_list.pop()
    for i in exist_list:
        i = int(i)
        top_five.append(i)
    exist_list = []
    
    user = int(input('Enter Your High Score: '))
    top_five.append(user)
    top_five.sort(reverse=True)
    print (top_five)
    
    file = open ('Store_score.txt','w')
    
    for i in top_five[0:5]:
        file.write(str(i)+'\n')
        
    file.close()
    top_five.clear()

def see_list():
    file = open ('Store_score.txt','r')
    print (file.read())
    file.close()


run = True
#file = open('Store_score.txt','w')
#file.close()
top_five = []

while run == True: 
    print ('''
    Here are your options:
    1) Enter Score
    2) Look at TOP FIVE List of Scores
    3) Exit
    ''')


    choice = int(input('Enter your selection: '))

    if choice == 1:
        enter_score(top_five)
    elif choice == 2:
        see_list()
    elif choice == 3:
        run = False
