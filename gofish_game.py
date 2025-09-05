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
        print(player.name)
    
    print("Each player's hand:")
    for player in game.players:
        print(f"{player.name}'s Hand:")
        for card in player.hand:
            card.display()

game_test()

# TODO TESTING: Outside of the class, create a function with the following
# Create a gofish/game object
# Setup the game using the new method
# Print out the list of players
# BONUS: Print out each player's hand to check their cards!