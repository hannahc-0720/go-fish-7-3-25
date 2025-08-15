from deck import Deck
from player import Player

class GoFish_Game():
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.is_playing = True
    
    def game_setup(self, num_players):
        self.deal_pile = Deck()
        self.deal_pile.shuffle()

        for i in range(1, num_players + 1):
            player = Player(f"Player {i}")
            self.players.append(player)
        
        if num_players < 5:
            cards_to_deal = 7
        else:
            cards_to_deal = 5

        for i in range(cards_to_deal):
            for player in self.players:
                self.deck.deal_card_to_player(player)