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
            rand_index = random.randint(index + 1, len(self.deck_of_cards) - 1)
            current_card = self.deck_of_cards[index]
            # print("Index: {} Num: {}".format(index, rand_index))
            self.deck_of_cards[index] = self.deck_of_cards[rand_index]
            self.deck_of_cards[rand_index] = current_card

    def deal_one_card(self, player):
        if len(self.deck_of_cards) == 0:
            print("There are no more cards to be dealt.")
        else:
            card = random.choice(self.deck_of_cards)
            player.hand.append(card)
            self.deck_of_cards.remove(card)

    def display_deck(self):
        for card in self.deck_of_cards:
            card.display()

# deck = Deck()
# deck.display_deck()