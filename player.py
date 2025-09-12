class Player():
    def __init__(self, username):
        self.username = username
        self.hand = []
        self.score = 0

    def display_hand(self):
        for card in self.hand:
            card.print_card()
    
    def check_hand(self, ask_rank):
        for card in self.hand:
            pass

'''
p1 = Player("Hannah")
print(p1.username)
print(p1.hand)
'''