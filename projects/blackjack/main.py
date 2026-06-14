from deck import Deck
from hand import Hand


def show_hand(title, hand):
    print(f"\n{title}")

    for card in hand.cards:
        print(card)

    print("Score:", hand.value)


deck = Deck()
deck.shuffle()

player = Hand()
dealer = Hand()

# Initial cards

player.add_card(deck.deal())
player.add_card(deck.deal())

dealer.add_card(deck.deal())
dealer.add_card(deck.deal())

# Player turn

while True:

    show_hand("Player Hand", player)

    if player.value > 21:
        print("\nPlayer busts!")
        print("Dealer wins because player exceeded 21.")
        quit()

    choice = input("\nHit or Stand? (h/s): ").lower()

    if choice == "h":
        player.add_card(deck.deal())
    else:
        break

# Dealer turn

while dealer.value < 17:
    dealer.add_card(deck.deal())

show_hand("Dealer Hand", dealer)

# Determine winner

print("\n===== RESULT =====")

if dealer.value > 21:
    print("Dealer busts!")
    print("Player wins because dealer exceeded 21.")

elif player.value == 21:
    print("Player wins!")
    print("Winning condition: Blackjack (21 points).")

elif dealer.value == 21:
    print("Dealer wins!")
    print("Winning condition: Blackjack (21 points).")

elif player.value > dealer.value:
    print("Player wins!")
    print(
        f"Winning condition: higher score ({player.value} vs {dealer.value})."
    )

elif dealer.value > player.value:
    print("Dealer wins!")
    print(
        f"Winning condition: higher score ({dealer.value} vs {player.value})."
    )

else:
    print("Tie!")
    print(
        f"Both player and dealer have {player.value} points."
    )