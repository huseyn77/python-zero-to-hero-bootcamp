class Chips:

    def __init__(self, total=100):
        self.total = total

    def win_bet(self, amount):
        self.total += amount

    def lose_bet(self, amount):
        self.total -= amount