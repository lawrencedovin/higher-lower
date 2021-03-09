from art import logo, vs
from game_data import data
from random import randint

data_length = len(data) - 1

player_a = data[randint(0, data_length)]
player_b = data[randint(0, data_length)]
score = 0

def print_player(player):
    return f"{player['name']}, {player['description']}, from {player['country']}"

def play_game(player_a, player_b):
    print(logo)
    print(f'Current score: {score}')
    print(f'Compare A: {print_player(player_a)}')
    print(vs)
    print(f'Against B: {print_player(player_b)}')

play_game(player_a, player_b)
