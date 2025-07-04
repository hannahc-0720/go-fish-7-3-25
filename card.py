class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def display(self):
        print(f"{self.rank} of {self.suit}")

card1 = Card(10, "Hearts")
card2 = Card("King", "Diamonds")
card1.display()
card2.display()