# Feb 13 2023
 
'''
# Warmup
def countUP(maxNum):
    for i in range(1, maxNum+1):
        print (i)

def countDown(minNum):
    startNum = 20
    while startNum >= minNum:
        print(startNum)
        startNum -= 1

try:
    countDirection = input("which direction do you want to count?[UP/DOWN]: ").upper()
except(ValueError):
    print("Invalid Input")


if countDirection == 'UP':
    topNum = int(input("what is the top number you would like me to count to?: "))
    countUP(topNum)
elif countDirection == 'DOWN':
    bottomNum = int(input("enter a number below 20: "))
    countDown(bottomNum)
else:
    print("I don't understand. ")
'''

# Deeper into while loops

x = True

while x == True:
    print('''
    Menu:
    1) Funny Joke
    2) Best Pizza
    3) exit
    ''') #Triple quotes allow for multiline print statements

    a = True
    while a == True:
        try:
            ans = int(input('select number: '))
            if ans > 0 and ans < 4:
                a = False
        except:
            print("invalid input")

    if ans == 1:
        print("I am a joke")
    elif ans == 2:
        print("Any pizza except hawaiian")
    
