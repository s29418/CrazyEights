import random


class Deck:

    def __init__(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)

    def create_deck(self):
        suits = ['Pik', 'Kier', 'Trefl', 'Karo']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [(rank, suit) for suit in suits for rank in ranks]

    def draw_card(self):
        return self.cards.pop()

    def deal_cards(self, number_of_players):
        player_cards = [[] for _ in range(number_of_players)]

        for c in range(8):
            for player in player_cards:
                player.append(self.draw_card())

        return player_cards
