class Player():
    def __init__(self, username):
        self.username = username
        self.hand = []
        self.score = 0

    def display_hand(self):
        for card in self.hand:
            card.print_card()

'''
p1 = Player("Hannah")
print(p1.username)
print(p1.hand)
'''