# Author: Aadil Hussain
# Python Version: v3.10.4 64-bit

# Now that you have learned to use the random module. Use that module to create your own game, or 
# make the back-end of an existing game (ie. Rock/paper/scissors) . In this game you must use:
# 
# 1) The random module
import random
import time

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
        self.is_blackjack = False
        self.is_bust = False

    def deal_card(self):
        '''deals card to player hand'''
        cardval = random.randint(1,10)
        self.hand.append(cardval)
        del cardval

    def player_play(self):
        '''plays player turn'''
        while True:
            if sum(self.hand) == 21:
                print("You've got a blackjack!")
                self.is_blackjack = True
                break
            elif sum(self.hand) > 21:
                print(".. oooh you've got a bust")
                self.is_bust = True
                break

            print(f"this is the value of your hand: {sum(self.hand)}")
            hit_or_stand = num_query('What would you like to do:\n1)Hit\n2)Stand\nMake Selection: ')

            if hit_or_stand == 1:
                self.deal_card()
            elif hit_or_stand == 2:
                break
            else:
                print(f'invalid input, you entered {hit_or_stand}')
        # ask for hit or stand in a loop

def closest(players):
    player_hands = dict()
    for player in players:
        player_hands[player.name] = sum(player.hand)

    max_hand = None
    for player in players:
        if sum(player.hand) > 21:
            continue
        if not max_hand:
            max_hand = players.index(player)
        elif max_hand and sum(max_hand.hand) < sum(player.hand): #bigger than current max_hand
            max_hand = players.index(player)
    if max_hand == "":
        print("all players are bust")
        return "all players are bust"
    return max_hand

def leaderboard(players):
    '''displays the leaderboard of the players'''

    player_banks = dict()
    for player in players:
        player_banks[player.name] = player.bank

    sorted_leaderboard = sorted(player_banks.items(), key=lambda mydictpair: mydictpair[1])

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
del num_of_players

print("\nThe playerlist is as follows: ")
player_index = 0
for player in players:
    # don't display dealer playerobject to user
    if player.name == 'dealer':
        continue
    player_index += 1
    print(f"Player{player_index})", player.name)
del player_index

# Introduces blackjack
print("Welcome to blackjack: modified :)")
print('''
in this blackjack: aces are just a 1, you cannot split hands or double down.
All players will play against a dealer and whoever gets the closest to but below 21 will get $100
the dealer isn't exactly a dealer in this sense, but just the game's character you're meant to beat.
when you decide to quit the game, economy will be checked and winner will be declared.

good luck, have fun!
''')

global_loop = True
while global_loop:
    for player in players: # PRE ROUND loop
        player.hand = [] # clears all player hands
        player.is_blackjack = False
        player.is_bust = False

    # deal dealer hand
    players[0].deal_card()
    players[0].deal_card()

    print(f"The dealer's hand for the round: {sum(players[0].hand)}")

    for player in players: # PER ROUND menu handler loop
        # skip over dealer in playerloop
        if player.name == 'dealer':
            continue
        print(f"Current Player: {player.name}\nPlease make a selecion.")

        # processes user's selection
        while True:
            menu_select = num_query(menu)

            if menu_select == 1:
                player.deal_card()
                player.deal_card()
                player.player_play()
                break
            elif menu_select == 2:
                print("\n--------------------------------------\nCurrent Leaderboard:")
                print(leaderboard(players))
                print("--------------------------------------")
            elif menu_select == 3:
                print("game ending\ndrumroll pls.......")
                for i in range(5):
                    time.sleep(1)
                    print("...")
                print(f"The winner of the match was: {leaderboard(players)[0]}")
                print("thanks for playing blackjck: modified. byebye!")
                quit()
            else:
                print(f"invalid input, you entered: {menu_select}")
        if player.is_blackjack:
            print("A player has got a blackjack! The round ends. Player gets $100")
            player.bank += 100
            break
        
        closest(players)
