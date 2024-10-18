import random


# a list of all the suits
SUITS = ['C', 'D',
         'H', 'S']
# a list of all the ranks
RANKS = ['A', '2', '3', '4',
         '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K']


def get_52_deck() -> list[str]:
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck += f'{rank}{suit}'
    return deck


def throw_dice(faces=6) -> int:
    return random.choice(range(faces)) + 1


def pick_random(deck: list):
    return random.choice(deck)
