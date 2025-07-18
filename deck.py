from card import Card
import random
# imports the class from the code file it's in

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

class Deck():
    def __init__(self):
        self.deck_of_cards = []

        for suit in suits:
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.deck_of_cards.append(card)