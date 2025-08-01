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
                
    def shuffle(self):

        for index in range(len(self.deck_of_cards) - 1):
            num = random.randint(index + 1, len(self.deck_of_cards) - 1)
            temp = self.deck_of_cards[index]
            # print("Index: {} Num: {}".format(index, num))
            self.deck_of_cards[index] = self.deck_of_cards[num]
            self.deck_of_cards[num] = temp

    def display_deck(self):
        for card in self.deck_of_cards:
            card.display()

deck = Deck()
deck.display_deck()