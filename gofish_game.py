# TODO: Create a main/game python file and create a go fish/game class inside
# The constructor of the class should include a deck of cards object, a list of players, and a property that tracks if the game is still being played
# HINT: Don’t forget to import any necessary files/classes!

from deck import Deck
from player import Player

class GoFish_Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.is_playing = True

    def create_players(self):
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        self.players.append(Player(name1))
        self.players.append(Player(name2))

    def deal_initial_cards(self):
        for i in range(7):
            for player in self.players:
                self.deck.deal_cards(player)

    def start_game(self):
        self.deck.shuffle()
        self.create_players()
        self.deal_initial_cards()

        print("Game Start")
        for player in self.players:
            player.display_hand()