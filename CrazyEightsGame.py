import Deck
import Player


class CrazyEightsGame:

    def __init__(self, number_of_bots):
        self.deck = Deck
        self.players = self.add_bots(number_of_bots)


    def add_bots(self, number_of_bots):
        return [Player("Gracz")] + [Player(f"Bot {i + 1}") for i in range(number_of_bots)]

    def check_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wygrywa!")
                return True
        return False
