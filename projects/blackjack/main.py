from deck import Deck
from hand import Hand

deck = Deck()
deck.shuffle()

player = Hand()
dealer = Hand()

player.add_card(deck.deal())
player.add_card(deck.deal())

dealer.add_card(deck.deal())
dealer.add_card(deck.deal())

print("Player cards:")

for card in player.cards:
    print(card)

print("Player score:", player.value,"\n")

print("Dealer cards:")

for card in dealer.cards:
    print(card)

print("Dealer score:", dealer.value)