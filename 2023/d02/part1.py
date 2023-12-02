"""2023 D02"""
import sys

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

MAX = {'red': 12, 'green':  13, 'blue': 14}

def valid_game(game):
    for hand in game['hands']:
        for color, value in hand.items():
            if value > MAX[color]:
                return False
    return True

def solve(games):
    res = 0
    for game in games:
        if valid_game(game):
            res += game['id']
    return res

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n')
    games = map(parse_game, data)
    print(solve(games))
