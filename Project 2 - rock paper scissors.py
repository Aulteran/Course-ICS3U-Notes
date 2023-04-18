import random

# The options for the game
options = ['rock', 'paper', 'scissors']

# The menu
menu = '''
1) Play Round
2) See Leaderboard
3) Exit
Make a selection: '''

# The leaderboard
leaderboard = {}

# The AI's name
ai_name = random.choice(['Rocky', 'Paperboy', 'Scissorman'])

# The player's name
player_name = input('What is your name? ')

# The number of rounds played
rounds_played = 0

# The player's streak
player_streak = 0

# The AI's streak
ai_streak = 0

# The main game loop
while True:
    print(menu)
    selection = input()
    if selection == '1':
        print(f"\n{player_name}'s streak: {player_streak}")
        print(f"{ai_name}'s streak: {ai_streak}")
        print('\n')
        print('Rock...')
        print('Paper...')
        print('Scissors...')
        player_choice = input('What do you choose? (rock, paper, or scissors) ')
        ai_choice = random.choice(options)
        print(f'\n{player_name} chose {player_choice}')
        print(f'{ai_name} chose {ai_choice}\n')
        if player_choice == ai_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and ai_choice == 'scissors') or (player_choice == 'paper' and ai_choice == 'rock') or (player_choice == 'scissors' and ai_choice == 'paper'):
            print(f"{player_name} wins!")
            player_streak += 1
            ai_streak = 0
        else:
            print(f"{ai_name} wins!")
            ai_streak += 1
            player_streak = 0
        rounds_played += 1
    elif selection == '2':
        if rounds_played == 0:
            print('No rounds played yet.')
        else:
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
            print('\nLeaderboard:')
            for i, (name, score) in enumerate(sorted_leaderboard):
                print(f'{i+1}. {name}: {score}')
    elif selection == '3':
        break
    else:
        print('Invalid selection, please try again.\n')
        continue
    leaderboard[player_name] = player_streak
