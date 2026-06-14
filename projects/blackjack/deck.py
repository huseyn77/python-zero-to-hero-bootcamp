import random
from card import Card

suits = ("Hearts", "Diamonds", "Clubs", "Spades")

ranks = (
    "Two", "Three", "Four", "Five",
    "Six", "Seven", "Eight", "Nine",
    "Ten", "Jack", "Queen", "King", "Ace"
)


class Deck:

    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()