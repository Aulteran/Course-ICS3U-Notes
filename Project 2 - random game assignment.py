# Author: Aadil Hussain
# Python Version: v3.10.4 64-bit

# Now that you have learned to use the random module. Use that module to create your own game, or 
# make the back-end of an existing game (ie. Rock/paper/scissors) . In this game you must use:
# 
# 1) The random module
import random

# 2) Menu - Options
menu = '''
1) Play Round
2) See Leaderboard
3) Exit
Make a selection: '''

# 3) Create an A.I. to play against
# 4) Ask the user their name
# 5) Give the A.I a random name from a list of names
# 6) Display the winner
# 7) Store score (streak?) in a list. (NOTE: list will reset each time you run the program)
# 8) Make the game as robust as possible (ie. No possibility of error message displaying)

def num_query(prompt):
    '''gets int query from user without errors'''
    try:
        return int(input(prompt))
    except(ValueError):
        print("invalid input")

class Player:
    '''player object'''
    def __init__(self, name: str):
        self.name = name
        self.bank = 0
        self.hand = []

    def deal_card(self):
        raise NotImplementedError

    def player_play(self):
        '''plays player turn'''
        raise NotImplementedError

def leaderboard(players):
    '''displays the leaderboard of the players'''

    player_banks = dict()
    for player in players:
        player_banks[player.name] = player.bank

    sorted_leaderboard = sorted(player_banks.items(), key=lambda x:x[1])

    return sorted_leaderboard

# Creates Players

players = []

# Creates ai dealer before humans

players.append(Player("dealer"))

num_of_players = num_query("How many players will be playing: ")

for i in range(1, num_of_players+1):
    player = Player(input(f"Enter name for player {i}: "))
    players.append(player)
    print(f"Player {i} has been added as: {player.name}\n")

print("\nThe playerlist is as follows: ")
player_index = 0
for player in players:
    # don't display dealer playerobject to user
    if player.name == 'dealer':
        continue
    player_index += 1
    print(f"Player{player_index})", player.name)

# Introduces blackjack
print("Welcome to blackjack: modified :)")
print('''
in this blackjack: aces are just a 1, you cannot split hands or double down.
All players will play against a dealer and whoever gets the closest to but below 21 will get $100
the dealer isn't exactly a dealer in this sense, but just the game's character you're meant to beat.

good luck, have fun!
''')
      
for player in players:
    # skip over dealer in playerloop
    if player.name == 'dealer':
        continue
    print(f"Current Player: {player.name}\nPlease make a selecion.")
    
    while True:
        menu_select = num_query(menu)

        if menu_select == 1:
            player.player_play()
            break
        elif menu_select == 2:
            print("\n--------------------------------------\nCurrent Leaderboard:")
            print(leaderboard(players))
            print("--------------------------------------")
        elif menu_select == 3:
            print("thanks for playing blackjck: modified. byebye!")
            quit()
        else:
            print(f"invalid input, you entered: {menu_select}")
