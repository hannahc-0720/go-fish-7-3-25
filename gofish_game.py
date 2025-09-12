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
    
        for name in range(num_players):
            new_player = Player(f"Player {name}") # first player's name = 0
            self.players.append(new_player)

            if num_players < 5:
                for i in range(7):
                    self.deal_pile.deal_one_card(new_player)
            else:
                for i in range(5):
                    self.deal_pile.deal_one_card(new_player)

def game_test():
    game = GoFish_Game()
    game.game_setup(2)

    print("Players in the Game:")
    for player in game.players:
        print(player.username)
    print("")
    
    print("Each player's hand:\n")
    for player in game.players:
        print(f"{player.username}'s Hand:")
        for card in player.hand:
            card.display()
        print("")

game_test()