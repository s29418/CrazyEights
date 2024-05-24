import random


class Deck:

    def __init__(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)
        self.discard_pile = []

    def create_deck(self):
        suits = ['pik', 'kier', 'trefl', 'karo']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [(rank, suit) for suit in suits for rank in ranks]

    def draw_card(self):
        if not self.cards:
            self.reshuffle_deck()
        return self.cards.pop()

    def deal_cards(self, number_of_players):
        player_cards = [[] for _ in range(number_of_players)]
        for c in range(8):
            for player in player_cards:
                player.append(self.draw_card())
        return player_cards

    def reshuffle_deck(self):
        top_card = self.discard_pile.pop()
        self.cards = self.discard_pile
        random.shuffle(self.cards)
        self.discard_pile = [top_card]

    def add_to_discard_pile(self, card):
        self.discard_pile.append(card)

    def top_discard_card(self):
        return self.discard_pile[-1]

    def change_top_discard_suit(self, new_suit):
        rank, _ = self.discard_pile[-1]
        self.discard_pile[-1] = (rank, new_suit)
