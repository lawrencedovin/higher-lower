from art import logo, vs
from game_data import data
from random import randint
import os

def clear_screen():
    os.system("clear") # Linux - OSX
    os.system("cls") # Windows

def print_player(player):
    return f"{player['name']}, {player['description']}, from {player['country']}"

def play_game(score):
    clear_screen()
    data_length = len(data) - 1
    player_a = data[randint(0, data_length)]
    player_b = data[randint(0, data_length)]

    print(logo)
    if score > 0: print(f"You're right! Current score: {score}")
    print(f'Compare A: {print_player(player_a)}')
    print(vs)
    print(f'Against B: {print_player(player_b)}')
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == 'A': 
        if player_a['follower_count'] > player_b['follower_count']:
            score += 1
            play_game(score)
        else:
            print('Incorrect game over')
    elif guess == 'B':
        if player_b['follower_count'] > player_a['follower_count']:
            score += 1
            play_game(score)
        else:
            print('Incorrect game over')

play_game(0)
