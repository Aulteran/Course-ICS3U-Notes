import random
import time

# Set up the deck of cards
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(value, suit) for value in values for suit in suits]

# Set up the game
player_name = input("Enter your name: ")
ai_names = ['Bob', 'Alice', 'Charlie', 'David']
ai_name = random.choice(ai_names)
scores = {'player': 0, 'ai': 0}

# Define a function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            value += 10
        elif card[0] == 'A':
            value += 1
        else:
            value += int(card[0])
    return value

# Define a function to display the hands and scores
def display_game(player_hand, ai_hand, player_score, ai_score, show_ai_hand):
    print("Player's hand:", player_hand)
    print("Player's score:", player_score)
    if show_ai_hand:
        print(ai_name + "'s hand:", ai_hand)
        print(ai_name + "'s score:", ai_score)
    else:
        print(ai_name + "'s hand:", [ai_hand[0], "X"])
        print(ai_name + "'s score: ?", "\n")

# Start the game loop
while True:
    # Shuffle the deck and deal the cards
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    ai_hand = [deck.pop(), deck.pop()]

    # Display the initial hands and scores
    player_score = calculate_hand_value(player_hand)
    ai_score = calculate_hand_value([ai_hand[0]])
    display_game(player_hand, ai_hand, player_score, ai_score, False)

    # Player's turn
    while True:
        choice = input("Hit or stand? ")
        if choice.lower() == 'hit':
            player_hand.append(deck.pop())
            player_score = calculate_hand_value(player_hand)
            display_game(player_hand, ai_hand, player_score, ai_score, False)
            if player_score > 21:
                print("Player busts!")
                scores['ai'] += 1
                break
        elif choice.lower() == 'stand':
            break

    # AI's turn
    if player_score <= 21:
        while ai_score < 17:
            ai_hand.append(deck.pop())
            ai_score = calculate_hand_value(ai_hand)
            display_game(player_hand, ai_hand, player_score, ai_score, True)
            time.sleep(1)
        if ai_score > 21:
            print(ai_name + " busts!")
            scores['player'] += 1
        elif ai_score > player_score:
            print(ai_name + " wins!")
            scores['ai'] += 1
        elif ai_score < player_score:
            print(player_name + " wins!")
            scores['player'] += 1
        else:
            print("It's a tie!")
    print("Score:", scores, "\n")

    # Ask the player if they want to play again
    choice = input("Play again? ")
    if choice.lower() != 'yes':
        break