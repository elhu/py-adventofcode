"""2023 D02"""
import sys
from functools import reduce

def parse_hand(raw_hand):
    cubes = {}
    for cube in raw_hand.split(', '):
        parts = cube.split(' ')
        cubes[parts[1]] = int(parts[0])
    return cubes

def parse_game(raw_game):
    parts = raw_game.split(': ')
    return {
        'id': int(parts[0].split(' ')[1]),
        'hands': map(parse_hand, parts[1].split('; '))
    }

def compute_power(game):
    maxs = {'red': 0, 'green': 0, 'blue': 0}
    for hand in game['hands']:
        for color, value in hand.items():
            if value > maxs[color]:
                maxs[color] = value
    return maxs['red'] * maxs['green'] * maxs['blue']

def solve(games):
    return reduce(lambda acc, game: acc + compute_power(game), games, 0)

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n')
    games = map(parse_game, data)
    print(solve(games))
