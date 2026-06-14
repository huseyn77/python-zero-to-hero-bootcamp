class Hand:

    values = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
    }

    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.values[card.rank]

        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21:
            for card in self.cards:
                if card.rank == "Ace":
                    self.value -= 10
                    return