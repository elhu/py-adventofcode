import sys
from functools import cmp_to_key

CARD_VALUES = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10
}

def parse_card_value(card):
    if card in CARD_VALUES:
        return CARD_VALUES[card]
    return int(card)

def parse_hand(hand):
    cards = {l: 0 for l in hand}
    for l in hand:
        cards[l] += 1
    hand_rank = 0
    if 5 in cards.values():
        hand_rank = 6
    elif 4 in cards.values():
        hand_rank = 5
    elif 3 in cards.values() and 2 in cards.values():
        hand_rank = 4
    elif 3 in cards.values():
        hand_rank = 3
    elif list(cards.values()).count(2) == 2:
        hand_rank = 2
    elif 2 in cards.values():
        hand_rank = 1
    hand_value = [hand_rank]
    hand_value.extend([parse_card_value(l) for l in hand])
    return hand_value

def compare_hands(l, r):
    a = l[1]
    b = r[1]
    for k in range(len(a)):
        if a[k] > b[k]:
            return 1
        elif a[k] < b[k]:
            return -1
    return 0

with open(sys.argv[1], 'r') as file:
    data = file.read().strip().split('\n')
    hands = [(hand.split()[0], parse_hand(hand.split()[0]), int(hand.split()[1])) for hand in data]
    hands = sorted(hands, key=cmp_to_key(compare_hands))
    sum = 0
    for idx, hand in enumerate(hands):
        sum += (idx+1)*hand[2]
    print(sum)
