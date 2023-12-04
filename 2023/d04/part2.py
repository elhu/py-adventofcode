"""2023 day 04"""

from functools import cache
import re
import sys

class CardsWonComputer:
    def __init__(self, wins):
        self.wins = wins

    def total_cards_won(self):
        return sum([self._compute_cards_won(i) for i in range(len(self.wins))])

    @cache
    def _compute_cards_won(self, index):
        return 1 + sum([self._compute_cards_won(i) for i in range(index+1, index+self.wins[index]+1)])


def compute_wins_per_card(cards):
    return list(map(lambda card: len(set(card[0]) & set(card[1])), cards))

def solve(cards):
    wins = compute_wins_per_card(cards)
    return CardsWonComputer(wins).total_cards_won()

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n')
    def parse_line(line):
        parts = re.split(r'(?:: | \| )', line)
        left = [int(x) for x in re.split('\s+', parts[1].strip())]
        right = [int(x) for x in re.split('\s+', parts[2].strip())]
        return left, right

    print(solve([parse_line(line) for line in data]))
